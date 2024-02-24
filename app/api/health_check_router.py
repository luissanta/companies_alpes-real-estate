from fastapi import APIRouter, status

health_check_router = APIRouter(
    tags=["health check"]
)


@health_check_router.get("/", status_code=status.HTTP_200_OK)
async def health_check() -> str:
    return "pong"
