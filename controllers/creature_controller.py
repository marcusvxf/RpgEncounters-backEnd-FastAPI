from sqlalchemy.orm import Session
from models import creature_model
from schemas import creature_schemas 
from controllers import base_controller
from sqlalchemy import func
from sqlalchemy.orm import joinedload

class creature_controller(base_controller.controller):

    default_attack_class = {}
    def __init__(self,default_class_value = None,class_attack = None):
        self.default_class = default_class_value
        self.default_attack_class = class_attack

    async def get(self,db:Session,id):
        query = db.query(self.default_class).get(id)
        return query

    async def list_all_unique(self,db:Session,limit:int = 100, skip:int=0):
        subquery = (
            db.query(
                self.default_class.name,
                func.min(self.default_class.id).label('min_id')
            )
            .group_by(self.default_class.name)
            .subquery()
        )

        query = (
            db.query(self.default_class)
            .join(subquery, self.default_class.id == subquery.c.min_id)
        )
        creatures = query.offset(skip).limit(limit).all()
        return creatures
    
    async def add_attack(self,db:Session,attack_class,creature_id:int,attack_id:int):
        creature = db.query(self.default_class).filter(self.default_class.id == creature_id).first()
        attack = db.query(attack_class).filter(attack_class.id == attack_id).first()
        creature.attacks.append(attack)

        db.add(creature)
        db.commit()
        db.refresh(creature)

        return True

class creature_attack_controller(base_controller.controller):
    async def list_all_unique(self,db:Session,limit:int = 100, skip:int=0):
        return