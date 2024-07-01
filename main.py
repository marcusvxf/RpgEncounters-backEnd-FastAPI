from typing import Union
from routers import encounter,campaign
from fastapi import FastAPI

from database import engine, Base

app = FastAPI()


app.include_router(encounter.router)
app.include_router(campaign.router)

@app.get("/")
async def root():
    return {"message": "Olá a api de encontros de RPG"}