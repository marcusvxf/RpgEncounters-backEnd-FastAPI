from typing import Union

from pydantic import BaseModel

class CampaignCreator(BaseModel):
    name:str
    description: Union[str, None] = None

class Campaign(BaseModel):
    id:int
    name:str
    description:str
    is_active:bool