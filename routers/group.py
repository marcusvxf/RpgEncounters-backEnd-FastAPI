from fastapi import APIRouter,Depends
from controllers import campaign_controller
from schemas import group_schemas
from database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(prefix="/group",
    tags=["group"],
    responses={404: {"description": "Not found"}},)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def list_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    return {"data":[]}



