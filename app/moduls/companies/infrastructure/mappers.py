import uuid
from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.companies.domain.entities import Company,List_Company
from app.moduls.companies.domain.value_objects import  Name,Location,Type
from .dto import Company as CompanyDTO, List_company as ListCompanyDTO

from datetime import datetime


class MapeadorCompany(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_companies(self, list_estate: List_Company) -> CompanyDTO:
        return [CompanyDTO(id=str(item.id), name=item.name, location=item.location, typeCompany=item.typeCompany) for item in list_estate.companies]

    def _procesar_companies_dto(self, list_estate_dto: ListCompanyDTO) -> Company:
        return [Company(estate_id=str(item.id), code=item.code, name=item.name) for item in list_estate_dto]

    def get_type(self) -> type:
        return List_Company.__class__

    def entity_to_dto(self, list_entidad: List_Company) -> ListCompanyDTO:
        list_dto = ListCompanyDTO()
        list_dto.companies = list()

        if not list_entidad:
            return list_dto

        list_dto.id = str(uuid.uuid4())
        list_dto.createdAt = datetime.now()
        # list_dto.updatedAt = datetime.now()

        estates_entity: list[Company] = list_entidad.companies

        list_dto.companies.extend(self._procesar_companies(estates_entity))

        return list_dto

    def dto_to_entity(self, dto: ListCompanyDTO) -> List_Company:
        list_estates = List_Company()
        list_estates.companies = list()
        if not dto:
            return list_estates

        list_estates.createdAt = datetime.now()    

        estates_dto: list[CompanyDTO] = dto.companies

        list_estates.companies.extend(self._procesar_companies_dto(estates_dto))

        return list_estates
