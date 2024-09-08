from typing import Union

from pydantic import BaseModel

class CreatureCreator(BaseModel):
    name:str
    challenger_level: float
    life_points_dice_qtd: int
    life_points_dice_type: int
    life_points_dice_bonus: int
    encounter_id:int

class Creature(BaseModel):
    id:int
    name:str
    challenger_level: float
    is_active:bool
    encounter_id:int
    