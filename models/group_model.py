from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Group(Base):
    __tablename__ = "tb_group"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    is_active = Column(Boolean, default=True)
    
    heroes = relationship("tb_hero",back_populates="group")
    encounters = relationship("tb_encounter",back_populates="group")


