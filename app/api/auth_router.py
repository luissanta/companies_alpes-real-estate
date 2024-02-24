from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(tags=["auth"])


@auth_router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    access_token = {"access_token": form_data.username + "token", "token_type": "bearer"}
    return access_token
