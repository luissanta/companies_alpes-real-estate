""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de lists
"""
from typing import List
from ..domain.entities import Estate
from ..domain.repository import ListRepository


class ListRepositoryPostgres(ListRepository):
    def get_by_id(self, entity_id: int) -> Estate:
        # TODO
        raise NotImplementedError

    def get_all(self) -> List[Estate]:
        # TODO
        raise NotImplementedError

    def create(self, entity: Estate):
        # TODO
        raise NotImplementedError

    def update(self, entity_id: int,  entity: Estate):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: int):
        # TODO
        raise NotImplementedError
