from fastapi import APIRouter
from app.moduls.lists.aplication.services import ListService

list_router = APIRouter(
    tags=["list"]
)


@list_router.get("/list")
async def get_list():
    list_service = ListService()
    return list_service.get_all_list()
