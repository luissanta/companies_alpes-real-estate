
from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.companies.domain.entities import Company
from app.moduls.companies.domain.value_objects import  Name, Location, Type
from .dto import CompanyDTO
import uuid
from datetime import datetime

class MapeadorCompanyDTOJson(AppMap):
    def _procesar_estate(self, company: dict) -> CompanyDTO:

        company_dto: CompanyDTO = CompanyDTO(company.get('name'), company.get('location'),company.get('typeCompany'))
        return company_dto
    
    def external_to_dto(self, externo: dict) -> CompanyDTO:
        dto = CompanyDTO(
            id=str(uuid.uuid4()),
            name=externo.get("name"),
            location=externo.get("location"),
            typeCompany=externo.get("typeCompany")
        )

        return dto

    def dto_to_external(self, dto: CompanyDTO) -> dict:
        if isinstance(dto, CompanyDTO):
            return dto.__dict__
        else:
            return dto

class MapeadorCompany(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def _procesar_companies(self, company_dto: CompanyDTO) -> Company:
                
        return Company(name=company_dto.name, location=company_dto.location, typeCompany=company_dto.typeCompany)
    
    def get_type(self) -> type:
        return Company.__class__

    def entity_to_dto(self, company: Company) -> CompanyDTO:        

        company_dto = CompanyDTO(id=str(company.id), name=company.name, location=company.location, typeCompany=company.typeCompany)

        return company_dto

    def dto_to_entity(self, dto: CompanyDTO) -> Company:
      
        if type(dto) == list:
            companies=[]
            for item in dto:
                entidad = Company(
                id=item.id,
                name=item.name,
                location=item.location,
                typeCompany=item.typeCompany
                )
                companies.append(entidad)
                
            return companies    
        else:            
            entidad = Company(
                id=dto.id,
                name=dto.name,
                location=dto.location,
                typeCompany=dto.typeCompany
            )
            return entidad        
                    
            