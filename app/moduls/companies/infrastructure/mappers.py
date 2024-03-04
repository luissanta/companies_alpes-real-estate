import uuid
from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.companies.domain.entities import Company
from app.moduls.companies.domain.value_objects import  Name,Location,Type
from .dto import Company as CompanyDTO

from datetime import datetime


class MapeadorCompany(RepMap):


    def get_type(self) -> type:
        return Company.__class__
    
    def entity_to_dto(self, entidad: any)-> CompanyDTO:
        dto = CompanyDTO(
            id=str(entidad.id),
            name=entidad.name,
            location=entidad.location,
            typeCompany=entidad.typeCompany
        )
        return dto

    def dto_to_entity(self, dto):
        entidad = Company(
            id=uuid.UUID(dto.id),
            name=dto.name,
            location=dto.location,
            typeCompany=dto.typeCompany
        )
        return entidad
