from fastapi import APIRouter,Depends
from controllers import creature_controller
from database import SessionLocal
from schemas import creature_schemas
from sqlalchemy.orm import Session
from models import creature_model


router = APIRouter(prefix="/attack",
    tags=["attack"],
    responses={404: {"description": "Not found"}},)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=creature_schemas.CreatureActions)
async def create_creature(creature_data:creature_schemas.CreateCreatureActions, db: Session = Depends(get_db)):
    creature = creature_controller.creature_attack_controller()
    data = await creature.create(db, creature_model.CreatureActions(**creature_data.dict()))
    return data

@router.get("/", response_model=list[creature_schemas.CreatureActions])
async def get_creature(limit:int = 100, skip:int=0, db: Session = Depends(get_db)):
    creature = creature_controller.creature_attack_controller(creature_model.CreatureActions)
    data = await creature.list_all(db,limit,skip)
    return data

