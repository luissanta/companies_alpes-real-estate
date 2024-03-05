from app.seedwork.aplication.queries import QueryHandler
from app.moduls.companies.infrastructure.factories import RepositoryFactory
from app.moduls.companies.domain.factory import CompanyFactory

class CreateCompanyBaseHandler(QueryHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._list_factories: CompanyFactory = CompanyFactory()

    @property
    def repository_factory(self):
        return self._repository_factory
    
    @property
    def list_factories(self):
        return self._list_factories    