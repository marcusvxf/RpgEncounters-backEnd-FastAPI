from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table,Float
from sqlalchemy.orm import relationship

from database import Base


class Creature(Base):
    __tablename__ = "tb_creature"

    id = Column(Integer, primary_key=True)
    name = Column(String(245))
    description = Column(String(1000))
    life_points_dice_qtd = Column(Integer)
    life_points_dice_type = Column(Integer)
    life_points_dice_bonus = Column(Integer)
    challenger_level = Column(Float)
    encounter_id = Column(Integer,ForeignKey("tb_encounter.id"))
    
     
    is_active = Column(Boolean, default=True)
    encounter = relationship("Encounter",back_populates="creatures")


