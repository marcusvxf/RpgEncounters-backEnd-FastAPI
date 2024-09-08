from fastapi import APIRouter,Depends
from controllers import campaign_controller
from schemas import campaign_schemas
from database import SessionLocal
from sqlalchemy.orm import Session
from models import campaign_model

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
    campaing = campaign_controller.campaign_controller(campaign_model.Campaign)
    data = await campaing.list_all(db)
    return data

@router.post("/", response_model=campaign_schemas.Campaign)
async def create_campaign(campaign_data:campaign_schemas.CampaignCreator, db: Session = Depends(get_db)):
    campaing = campaign_controller.campaign_controller(campaign_model.Campaign)
    data = await campaing.create(db, campaign_model.Campaign(**campaign_data.dict()))
    return data

@router.delete("/", response_model=bool)
async def delete_campaign(campaign_id: int , db: Session = Depends(get_db)):
    campaing = campaign_controller.campaign_controller(campaign_model.Campaign)
    return await campaing.delete(db,campaign_id)

@router.put("/", response_model=campaign_schemas.Campaign)
async def update_campaign(campaign_data:campaign_schemas.CampaignCreator, db: Session = Depends(get_db)):
    campaign = campaign_controller.campaign_controller(campaign_model.Campaign)
    result = await campaign.update(db,campaign_data.id,campaign_data)
    return result