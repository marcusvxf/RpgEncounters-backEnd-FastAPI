from typing import Union

from pydantic import BaseModel

class CreatureCreator(BaseModel):
    name:str
    level:int
    challenger_level: int
    life_points_dice_qtd: int
    life_points_dice_type: int
    life_points_dice_bonus: int

class Creature(BaseModel):
    id:int
    name:str
    level:int
    challenger_level: int
    is_active:bool
    