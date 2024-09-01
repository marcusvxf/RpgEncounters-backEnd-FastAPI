from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table
from sqlalchemy.orm import relationship

from database import Base
from models import group_model


class Campaign(Base):
    __tablename__ = "tb_campaign"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    description = Column(String(500))
    is_active = Column(Boolean, default=True)
    
    encounters = relationship("Encounter",back_populates="campaigns")
    groups = relationship("Group",secondary=group_model.group_campaign,back_populates="campaigns")

