from sqlalchemy.orm import Session
from models import campaign_model
from schemas import campaign_schemas 

async def list_my_campaigns(db:Session,limit:int = 100, skip:int=0):
    query = db.query(campaign_model.Campaign).offset(skip).limit(limit).all()
    return [query]

async def create_campaign(db: Session, data: campaign_schemas.CampaignCreator):
    db_campaign = campaign_model.Campaign(**data.dict())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign