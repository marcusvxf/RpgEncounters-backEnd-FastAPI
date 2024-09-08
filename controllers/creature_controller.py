from sqlalchemy.orm import Session
from models import creature_model
from schemas import creature_schemas 
from controllers import base_controller

class creature_controller(base_controller.controller):
    async def list_my(self,db:Session,limit:int = 100, skip:int=0):
       
        return 