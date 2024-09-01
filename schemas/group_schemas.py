from typing import Union

from pydantic import BaseModel

class GroupCreator(BaseModel):
    name:str
    description: Union[str, None] = None

class Group(BaseModel):
    id:int
    name:str
    is_active:bool