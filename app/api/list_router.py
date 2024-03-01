import json
from typing import Any, Dict
from fastapi import APIRouter, Request, Response, status
from pydantic import BaseModel

from app.moduls.lists.aplication.querys.get_states import GetEstate
from app.moduls.lists.aplication.services import ListService
from app.moduls.lists.aplication.mappers import MapeadorEstateDTOJson as MapApp
from app.moduls.lists.aplication.commands.create_estate import CreateEstate
from app.seedwork.domain.exceptions import DomainException

from app.seedwork.aplication.commands import execute_command
from app.seedwork.aplication.queries import execute_query

list_router = APIRouter(
    tags=["list"]
)


@list_router.get("/list", status_code=status.HTTP_200_OK)
async def get_list():
    map_estates = MapApp()
    sr = ListService()
    return map_estates.dto_to_external(sr.get_all_list())

@list_router.get("/listQuery", status_code=status.HTTP_200_OK)
def get_estate_using_query(id=None):
    query_resultado = execute_query(GetEstate(id))
    map_estates = MapApp()
    
    return map_estates.dto_to_external(query_resultado.resultado)

@list_router.post("/estate-command", status_code=status.HTTP_201_CREATED)
def async_create_state(data: Dict[str, Any]):
    try:
        estate_dict = data

        print("Request.json: ", estate_dict)
        map_estate = MapApp()
        estate_dto = map_estate.external_to_dto(estate_dict)

        command = CreateEstate(estate_dto.id, estate_dto.code, estate_dto.name)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        execute_command(command)
        
        return map_estate.dto_to_external(estate_dto) #Response('{}', status=201, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
