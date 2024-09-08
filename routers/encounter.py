from fastapi import APIRouter,Depends
from controllers import encounter_controller
from database import SessionLocal
from schemas import encounter_schemas
from sqlalchemy.orm import Session
from models import encounter_model


router = APIRouter(prefix="/encounter",
    tags=["encounter"],
    responses={404: {"description": "Not found"}},)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[encounter_schemas.Encounter])
async def list_encounters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    encounter =encounter_controller.encounter_controller(encounter_model.Encounter)
    data = await encounter.list_all(db)
    return data


@router.post("/", response_model=encounter_schemas.Encounter)
async def create_encounter(encounter_data:encounter_schemas.EncounterCreator, db: Session = Depends(get_db)):
    encounter = encounter_controller.encounter_controller(encounter_model.Encounter)
    data = await encounter.create(db, encounter_model.Encounter(**encounter_data.dict()))
    return data

