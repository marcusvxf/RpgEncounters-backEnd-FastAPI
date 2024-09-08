from sqlalchemy.orm import Session
from controllers import base_controller

class campaign_controller(base_controller.controller):
    async def list_my(self,db:Session,limit:int = 100, skip:int=0):
       
        return 