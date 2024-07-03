from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Encounter(Base):
    __tablename__ = "tb_encounter"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, index=True)
    is_active = Column(Boolean, default=True)
    campaign_id = Column(Integer,ForeignKey("tb_campaign.id"))
    group_id = Column(Integer,ForeignKey("tb_group.id"))


    campaign = relationship("tb_campaign",back_populates="encounters")
    group = relationship("tb_group",back_populates="encounters")

