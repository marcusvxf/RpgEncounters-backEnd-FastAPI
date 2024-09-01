from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table
from sqlalchemy.orm import relationship
from models import hero_model,encounter_model


from database import Base

group_campaign = Table('group_campaign',Base.metadata,
                    Column('campaign_id', ForeignKey('tb_campaign.id'),primary_key=True),
                    Column('group_id', ForeignKey('tb_group.id'),primary_key=True)
                    )

class Group(Base):
    __tablename__ = "tb_group"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    is_active = Column(Boolean, default=True)

    encounters = relationship("Encounter",back_populates="groups")
    heroes = relationship("Hero",back_populates="group")
    campaigns = relationship("Campaign",secondary=group_campaign,back_populates="groups")


