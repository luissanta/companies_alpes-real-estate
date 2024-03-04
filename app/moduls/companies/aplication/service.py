from app.seedwork.aplication.services import Service
from ..aplication.dto import CompanyDTO
from app.moduls.companies.domain.factory import CompanyFactory
from app.moduls.companies.infrastructure.factories import RepositoryFactory
from ..domain.repositories import CompanyRepository
from .mappers import MapeadorCompany

class CompanyService(Service):

    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._list_factories: CompanyRepository = CompanyRepository()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def list_factory(self):
        return self._list_factories

    def get_all_list(self) -> CompanyDTO:
        repository = self.repository_factory.create_object(CompanyRepository.__class__)        
        return self.list_factory.create_object(repository.get_all(), MapeadorCompany())
    
    def get_all(self) -> CompanyDTO:
        repository = self.repository_factory.create_object(CompanyRepository.__class__)
        
        return self.list_factory.create_object(repository.get_all(), MapeadorCompany())
