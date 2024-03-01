from pydantic import BaseModel
from fastapi import HTTPException, FastAPI, Response, Depends
from uuid import UUID, uuid4

from fastapi_sessions.backends.implementations import InMemoryBackend
#from fastapi_sessions.session_verifier import SessionVerifier
#from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters

session = uuid4()

class SessionData(BaseModel):
    username: str

backend = InMemoryBackend[UUID, SessionData]()

async def create_session():
    data = SessionData(username='uow')
    print(data)
    await backend.create(session, data)

async def get_session():
    datanew = backend.read(session)
    print(datanew)
    return datanew
