from fastapi import APIRouter,Depends
from controllers import creature_controller
from database import SessionLocal
from schemas import creature_schemas
from sqlalchemy.orm import Session
from models import creature_model


router = APIRouter(prefix="/creature",
    tags=["creature"],
    responses={404: {"description": "Not found"}},)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=creature_schemas.Creature)
async def create_creature(creature_data:creature_schemas, db: Session = Depends(get_db)):
    creature = creature_controller.creature_controller(creature_model.Creature)
    data = await creature.create(db, creature_model.Creature(**creature_data.dict()))
    return data

@router.get("/{creature_id}", response_model=creature_model.Creature)
async def get_creature(creature_id:int, db: Session = Depends(get_db)):
    campaing = creature_controller.creature_controller(creature_model.Creature)
    data = await campaing.get(db,creature_id)
    return data
