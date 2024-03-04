

from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repository
from .exceptions import FactoryException
from .repositories import CompanyRepositoryPostgres
from ..domain.repositories import CompanyRepository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == CompanyRepository.__class__:
            return CompanyRepositoryPostgres()
        else:
            raise FactoryException
