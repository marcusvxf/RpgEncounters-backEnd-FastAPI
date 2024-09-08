from typing import Union

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