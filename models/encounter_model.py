from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models import group_model,creature_model

from database import Base


class Encounter(Base):
    __tablename__ = "tb_encounter"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), index=True)
    description = Column(String(500))
    is_active = Column(Boolean, default=True)
    campaign_id = Column(Integer,ForeignKey("tb_campaign.id"))
    group_id = Column(Integer,ForeignKey("tb_group.id"))


    groups = relationship("Group",back_populates="encounters")
    campaigns = relationship("Campaign",back_populates="encounters")
    creatures = relationship("Creature",back_populates="encounter")

