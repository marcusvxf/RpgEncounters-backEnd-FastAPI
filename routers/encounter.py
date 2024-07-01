from fastapi import APIRouter
from ..controllers import encounter_controller

router = APIRouter(prefix="/encounter",
    tags=["encounter"],
    responses={404: {"description": "Not found"}},)

@router.get("/", tags=["encounter"])
async def list_encounters():
    data = await encounter_controller.list_my_encounters()
    return {"data":data}

@router.get("/{item_id}", tags=["encounter"])
async def list_encounters(item_id:str):
    return [{"username": "Rick"}, {"username": "Morty"}]

