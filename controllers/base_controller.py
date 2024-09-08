from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class controller():
    default_class = {}
    def __init__(self,default_class_value = None):
        self.default_class = default_class_value

    async def list_all(self,db:Session,limit:int = 100, skip:int=0):
        query = db.query(self.default_class).offset(skip).limit(limit).all()
        return query
    
    async def get(self,db:Session,id):
        query = db.get(self.default_class,id)
        return query
    
    async def create(self,db: Session, data_to_create):
        db_table = data_to_create
        db.add(db_table)
        db.commit()
        db.refresh(db_table)
        return db_table
    
    async def delete(self,db: Session, id_to_delete):
        item_to_delete = db.get(self.default_class,id_to_delete)
        db.delete(item_to_delete)
        db.commit()
        return True
    
    async def update(self,db: Session, id_to_update,data_to_update):
        item_to_update = db.get(self.default_class,id_to_update)
        item_to_update.sqlmodel_update(data_to_update)
        db.add(item_to_update),
        db.commit()
        db.refresh(item_to_update)
        return item_to_update