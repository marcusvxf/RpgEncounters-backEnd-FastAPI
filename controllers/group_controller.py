from models import group_model
from sqlalchemy.orm import Session
from schemas import group_schemas

async def list_my(db:Session,limit:int = 100, skip:int=0):
    query = db.query(group_model.Group).offset(skip).limit(limit).all()
    return [query]
