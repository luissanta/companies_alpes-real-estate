""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos
"""

from app.config.db import SessionLocal
from .dto import Listado as ListadoDTO
from app.moduls.lists.domain.entities import List
from ..domain.repositories import ListRepository


class EstateRepositoryPostgres(ListRepository):

    def get_by_id(self, id: int) -> List:
        # TODO
        raise NotImplementedError

    def get_all(self) -> list[List]:
        session = SessionLocal()
        reserva_dto = session.query(ListadoDTO).all()
        estate_list = [List(id=item.id, code=item.code, name=item.name) for item in reserva_dto]
        return [estate_list]

    def create(self, entity: List):
        # TODO
        raise NotImplementedError

    def update(self, entity_id: int, entity: List):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: int):
        # TODO
        raise NotImplementedError
