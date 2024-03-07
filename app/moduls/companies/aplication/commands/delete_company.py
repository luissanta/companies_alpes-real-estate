from app.seedwork.aplication.commands import Command
from app.moduls.companies.aplication.dto import CompanyDTO
from .base import CreateCompanyBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplication.commands import execute_command as command

from app.moduls.companies.domain.entities import Company
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.moduls.companies.aplication.mappers import MapeadorCompany
from app.moduls.companies.infrastructure.repositories import CompanyRepository


@dataclass
class DeleteCompany(Command):
    id: str 
    

class DeleteCompanyHandler(CreateCompanyBaseHandler):
    
    def handle(self, command: DeleteCompany):
        company_id = str(command.id)       
        # company: Company = self.list_factories.create_object(company, MapeadorCompany())
        # company.delete_company(company.id)
        repository = self.repository_factory.create_object(CompanyRepository.__class__)

        UnitOfWorkPort.regist_batch(repository.delete(company_id))
        UnitOfWorkPort.savepoint()
        # UnitOfWorkPort.commit()


@command.register(DeleteCompany)
def execute_command_delete_company(comando: DeleteCompany):
    handler = DeleteCompanyHandler()
    handler.handle(comando)