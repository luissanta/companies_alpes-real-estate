from fastapi import APIRouter, status
from app.moduls.lists.aplication.services import ListService

list_router = APIRouter(
    tags=["list"]
)


@list_router.get("/list", status_code=status.HTTP_200_OK)
async def get_list():
    sr = ListService()
    return sr.get_list_by_id(id)
