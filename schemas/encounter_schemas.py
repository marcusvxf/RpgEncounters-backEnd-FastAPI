from typing import Union
from schemas import creature_schemas

from pydantic import BaseModel

class EncounterCreator(BaseModel):
    name:str
    description: Union[str, None] = None
    campaign_id:Union[int, None] = None

class Encounter(BaseModel):
    id:int
    name:str
    description: Union[str, None] = None
    campaign_id:Union[int, None] = None
    group_id:Union[int, None] = None
    is_active:bool

class EncounterDetails(BaseModel):
    id:int
    name:str
    description: Union[str, None] = None
    campaign_id:Union[int, None] = None
    group_id:Union[int, None] = None
    creatures: list[creature_schemas.Creature]
    is_active:bool