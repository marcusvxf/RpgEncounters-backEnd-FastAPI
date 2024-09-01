from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table
from sqlalchemy.orm import relationship

from database import Base

encounter_creature = Table('encounter_creature',Base.metadata,
                    Column('encounter_id', ForeignKey('tb_encounter.id'),primary_key=True),
                    Column('creature_id', ForeignKey('tb_creature.id'),primary_key=True)
                    )


class Creature(Base):
    __tablename__ = "tb_creature"

    id = Column(Integer, primary_key=True)
    level = Column(Integer)
    life_points_dice_qtd = Column(Integer)
    life_points_dice_type = Column(Integer)
    life_points_dice_bonus = Column(Integer)
    challenger_level = Column(Integer)
    description = Column(String(1000))
    name = Column(String(245))
    
     
    is_active = Column(Boolean, default=True)
    encounters= relationship("Encounter",secondary=encounter_creature,back_populates="creatures")


