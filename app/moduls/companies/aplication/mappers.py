
from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.companies.domain.entities import Company,List_Company
from app.moduls.companies.domain.value_objects import  Name, Location, Type
from .dto import CompanyDTO,ListCompanyDTO

from datetime import datetime

class MapeadorCompanyDTOJson(AppMap):
    def _procesar_estate(self, company: dict) -> CompanyDTO:

        company_dto: CompanyDTO = CompanyDTO(company.get('name'), company.get('location'),company.get('typeCompany'))
        return company_dto
    
    def external_to_dto(self, externo: dict) -> ListCompanyDTO:

        list_dto = ListCompanyDTO()

        companies: list[CompanyDTO] = list()
        for itin in externo.get("companies"):
            list_dto.companies.append(self._procesar_estate(itin))

        return list_dto

    def dto_to_external(self, dto: ListCompanyDTO) -> dict:
        return dto.__dict__

class MapeadorCompany(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def _procesar_companies(self, company_dto: CompanyDTO) -> Company:
        return Company(name=company_dto.name, location=company_dto.location, typeCompany=company_dto.typeCompany)
    
    def get_type(self) -> type:
        return Company.__class__

    def entity_to_dto(self, list_entidad: List_Company) -> ListCompanyDTO:
        list_dto = ListCompanyDTO()

        for estates_entity in list_entidad.estates:
            estate_dto = CompanyDTO(id=estates_entity.id, name=estates_entity.name, code=estates_entity.code)
            list_dto.estates.append(estate_dto) 

        return list_dto

    def dto_to_entity(self, dto: ListCompanyDTO) -> List_Company:
        list_estates = List_Company()
        list_estates.companies = list()

        estates_dto: list[CompanyDTO] = dto.companies

        for itin in estates_dto.companies:
            list_estates.companies.append(self._procesar_companies(itin))
            
        return list_estates