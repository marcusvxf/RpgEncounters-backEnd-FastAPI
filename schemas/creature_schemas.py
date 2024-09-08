from typing import Union

from pydantic import BaseModel

class CreatureActions(BaseModel):
    id:int
    name:str
    description:str
    dice_qtd: int
    dice_type: int
    dice_bonus: int

class CreateCreatureActions(BaseModel):
    name:str
    description:str
    dice_qtd: int
    dice_type: int
    dice_bonus: int
class CreatureCreator(BaseModel):
    name:str
    challenger_level: float
    life_points_dice_qtd: int
    life_points_dice_type: int
    life_points_dice_bonus: int
    encounter_id:Union[int,None] = None

class Creature(BaseModel):
    id:int
    name:str
    description:Union[str,None] = None
    challenger_level: float
    life_points_dice_qtd: int
    life_points_dice_type: int
    life_points_dice_bonus: int
    is_active:bool
    encounter_id:Union[int,None] = None
    attacks: list[CreatureActions]

