from fastapi import APIRouter,Depends
from controllers import encounter_controller
from database import SessionLocal
from schemas import encounter_schemas
from sqlalchemy.orm import Session


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
    data = await encounter_controller.list_my(db,limit,skip)
    return {"data":data}

@router.get("/{item_id}", response_model=list[encounter_schemas.Encounter])
async def list_encounters(campaign_data:encounter_schemas.EncounterCreator, db: Session = Depends(get_db)):
    encounter_created = await encounter_controller.create(db,campaign_data)
    return encounter_created

