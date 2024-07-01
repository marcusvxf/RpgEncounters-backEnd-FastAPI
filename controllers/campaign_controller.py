from sqlalchemy.orm import Session
from ..models import campaign_model

async def list_my_campaigns(db:Session,user_id:int,limit:int = 100, skip:int=0):
    query = db.query(campaign_model.Campaign).all()
    return [query]