from fastapi import APIRouter,Depends
from controllers import campaign_controller
from schemas import campaign_schemas
from database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(prefix="/campaign",
    tags=["campaign"],
    responses={404: {"description": "Not found"}},)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[campaign_schemas.Campaign])
async def list_campaign(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = await campaign_controller.list_my(db,limit,skip)
    return {"data":data}

@router.post("/", response_model=campaign_schemas.Campaign)
async def create_campaign(campaign_data:campaign_schemas.CampaignCreator, db: Session = Depends(get_db)):
    data = await campaign_controller.create(db,campaign_data)
    return data

