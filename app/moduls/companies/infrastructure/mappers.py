import uuid
from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.lists.domain.entities import Estate, List_estates
from app.moduls.lists.domain.value_objects import Code, Name
from .dto import Company as CompanyDTO

from datetime import datetime


class MapeadorCompany(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_estates(self, list_estate: List_estates) -> CompanyDTO:
        return [CompanyDTO(estate_id=str(item.id), code=item.code, name=item.name) for item in list_estate]

    def _procesar_estates_dto(self, list_estate_dto: CompanyDTO) -> Estate:
        return [Estate(estate_id=str(item.id), code=item.code, name=item.name) for item in list_estate_dto]

    def get_type(self) -> type:
        return List_estates.__class__

    def entity_to_dto(self, list_entidad: List_estates) -> CompanyDTO:
        list_dto = CompanyDTO()
        list_dto.estates = list()

        if not list_entidad:
            return list_dto

        list_dto.id = str(uuid.uuid4())
        list_dto.createdAt = datetime.now()
        list_dto.updatedAt = datetime.now()

        estates_entity: list[Estate] = list_entidad.estates

        list_dto.estates.extend(self._procesar_estates(estates_entity))

        return list_dto

    def dto_to_entity(self, dto: CompanyDTO) -> List_estates:
        list_estates = List_estates()
        list_estates.estates = list()
        if not dto:
            return list_estates

        list_estates.createdAt = datetime.now()
        list_estates.updatedAt = datetime.now()

        estates_dto: list[CompanyDTO] = dto.estates

        list_estates.estates.extend(self._procesar_estates_dto(estates_dto))

        return list_estates
