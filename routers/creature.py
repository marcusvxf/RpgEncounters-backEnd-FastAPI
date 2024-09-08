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

creature_controller_item = creature_controller.creature_controller(creature_model.Creature,creature_model.CreatureActions)


@router.post("/", response_model=creature_schemas.Creature)
async def create_creature(creature_data:creature_schemas.CreatureCreator, db: Session = Depends(get_db)):
    data = await creature_controller_item.create(db, creature_model.Creature(**creature_data.dict()))
    return data

@router.get("/{creature_id}", response_model=creature_schemas.Creature)
async def get_creature(creature_id:int, db: Session = Depends(get_db)):
    data = await creature_controller_item.get(db,creature_id)
    return data

@router.get("/", response_model=list[creature_schemas.Creature])
async def get_creature(limit:int = 100, skip:int=0, db: Session = Depends(get_db)):
    data = await creature_controller_item.list_all_unique(db,limit,skip)
    return data

@router.post("/{creature_id}/attack/{attack_id}", response_model=bool)
async def get_creature(creature_id:int,attack_id:int, db: Session = Depends(get_db)):
    data = await creature_controller_item.add_attack(db,creature_model.CreatureActions,creature_id,attack_id)
    return data

