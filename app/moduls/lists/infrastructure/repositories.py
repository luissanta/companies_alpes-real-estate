""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de lists
"""

from app.config.db import db
from .dto import Estate as EstateDTO
from app.moduls.lists.domain.entities import Estate
from app.moduls.lists.domain.repositories import ListRepository


class EstateRepositoryPostgres(ListRepository):

    def get_by_id(self, entity_id: int) -> EstateDTO:
        # TODO
        raise NotImplementedError

    def get_all(self) -> list[EstateDTO]:
        estate_dto = db.session.query(EstateDTO).all()
        try:    
            estate_list = [EstateDTO(id=item.id, code=item.code, name=item.name) for item in estate_dto]
        except Exception as e:
            print("Error: ",e)

        return estate_list

    def create(self, entity: Estate):
        # TODO
        estate = EstateDTO(id = entity.id, name = entity.name, code = entity.code)
        db.session.add(estate)

    def update(self, entity_id: int, entity: EstateDTO):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: int):
        # TODO
        raise NotImplementedError
