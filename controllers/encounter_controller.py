from sqlalchemy.orm import Session
from models import encounter_model
from controllers import base_controller
from schemas import encounter_schemas

class encounter_controller(base_controller.controller):
    async def list_my(self,db:Session,limit:int = 100, skip:int=0):

        return 