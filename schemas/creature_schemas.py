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
    name:str
    description:Union[str,None] = None
    challenger_level: float
    hit_points: int
    life_points_dice_qtd: int
    life_points_dice_type: int
    life_points_dice_bonus: int
    encounter_id:Union[int,None] = None
    strength: int
    dexterity: int
    intelligence: int
    charisma: int
    wisdom: int
    constitution: int
    st_strength: int
    st_dexterity: int
    st_intelligence: int
    st_charisma: int
    st_wisdom: int
    st_constitution: int
    languages: str
    immunities: Union[str,None] = None
    passive_perspective: Union[int,None] = None
    dark_vision: Union[int,None] = None

class Creature(BaseModel):
    id:int
    name:str
    description:Union[str,None] = None
    challenger_level: float
    hit_points: Union[int,None] = None
    life_points_dice_qtd: Union[int,None] = None
    life_points_dice_type: Union[int,None] = None
    life_points_dice_bonus: Union[int,None] = None
    is_active:bool
    encounter_id:Union[int,None] = None
    attacks: Union[list[CreatureActions],None] = None
    strength: Union[int,None] = None
    dexterity: Union[int,None] = None
    intelligence: Union[int,None] = None
    charisma: Union[int,None] = None
    wisdom: Union[int,None] = None
    constitution: Union[int,None] = None
    st_strength: Union[int,None] = None
    st_dexterity: Union[int,None] = None
    st_intelligence: Union[int,None] = None
    st_charisma: Union[int,None] = None
    st_wisdom: Union[int,None] = None
    st_constitution: Union[int,None] = None
    languages: Union[str,None] = None
    immunities: Union[str,None] = None
    passive_perspective: Union[int,None] = None
    dark_vision: Union[int,None] = None

