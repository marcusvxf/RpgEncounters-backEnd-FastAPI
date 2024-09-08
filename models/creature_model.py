from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table,Float
from sqlalchemy.orm import relationship

from database import Base

CreatureActions = Table('tb_n_creatures_n_actions',Base.metadata,
                    Column('creature_id', ForeignKey('tb_creature.id'),primary_key=True),
                    Column('attack_id', ForeignKey('tb_creature_action.id'),primary_key=True)
                    )

class Creature(Base):
    __tablename__ = "tb_creature"

    id = Column(Integer, primary_key=True)
    name = Column(String(245))
    description = Column(String(1000))
    life_points_dice_qtd = Column(Integer)
    life_points_dice_type = Column(Integer)
    life_points_dice_bonus = Column(Integer)
    challenger_level = Column(Float)
    armor_class = Column(Integer)
    alignment = Column(String(20))
    strength = Column(Integer)
    dexterity = Column(Integer)
    intelligence = Column(Integer)
    charisma = Column(Integer)
    wisdom = Column(Integer)
    constitution = Column(Integer)
    encounter_id = Column(Integer,ForeignKey("tb_encounter.id"))
    
     
    is_active = Column(Boolean, default=True)
    encounter = relationship("Encounter",back_populates="creatures")
    actions = relationship("CreatureActions",secondary=CreatureActions,back_populates="creatures")



class CreatureActions(Base):
    __tablename__ = "tb_creature_action"
    id = Column(Integer, primary_key=True)
    name = Column(String(245))
    description = Column(String(1000))
    dice_qtd = Column(Integer)
    dice_type = Column(Integer)
    dice_bonus = Column(Integer)
    creatures = relationship("Creature",secondary=CreatureActions,back_populates="actions")
