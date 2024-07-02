
from sqlalchemy.orm import Session
from models import encounter_model
from schemas import encounter_schemas


async def list_my(db:Session,limit:int = 100, skip:int=0):
    query = db.query(encounter_model.Encounter).offset(skip).limit(limit).all()
    return [query]

async def create(db: Session, data: encounter_schemas.EncounterCreator):
    db_encounter = encounter_schemas.Encounter(**data.dict())
    db.add(db_encounter)
    db.commit()
    db.refresh(db_encounter)
    return db_encounter