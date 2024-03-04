from app.moduls.companies.domain.exceptions import TipoObjetoNoExisteEnDominioCompanyExcepcion
from app.moduls.lists.domain.rules import EstateMinOne
from app.seedwork.domain.repositories import Mapper
from app.seedwork.domain.entities import Entity

from .entities import Company
from dataclasses import dataclass
from app.seedwork.domain.factories import Factory



@dataclass
class _CompanyFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            companies: Company = mapper.dto_to_entity(obj)

            #self.validate_rule(EstateMinOne(Estate.code))

            return companies


@dataclass
class CompanyFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        if mapper.get_type() == Company.__class__:
            list_factory = _CompanyFactory()
            return list_factory.create_object(obj, mapper)
        else:
            raise TipoObjetoNoExisteEnDominioCompanyExcepcion()
