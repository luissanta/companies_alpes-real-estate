from fastapi import APIRouter, status

health_check_router = APIRouter(
    tags=["health check"]
)


@health_check_router.get("/", status_code=status.HTTP_200_OK)
async def health_check() -> str:
    return "pong"

@health_check_router.get("/list1", status_code=status.HTTP_200_OK)
async def get_list():
    #if id:
    #    sr = ServicioListado()
        
    #    return sr.obtener_listado_por_id(id)
    #else:
    return [{'message': 'GET!'}]