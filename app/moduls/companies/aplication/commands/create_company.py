from app.seedwork.aplication.commands import Command
from app.moduls.companies.aplication.dto import CompanyDTO, ListCompanyDTO
from .base import CreateCompanyBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplication.commands import execute_command as command

from app.moduls.companies.domain.entities import List_Company
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.moduls.companies.aplication.mappers import MapeadorCompany
from app.moduls.companies.infrastructure.repositories import CompanyRepository

@dataclass
class CreateCompany(Command):
    companies: ListCompanyDTO

class CreateCompanyHandler(CreateCompanyBaseHandler):
    
    def handle(self, command: CreateCompany):
        companies = command
        
        estate_list: ListCompanyDTO = self.list_factories.create_object(companies, MapeadorCompany())
        estate_list.create_company(estate_list)
        repository = self.repository_factory.create_object(CompanyRepository.__class__)

        UnitOfWorkPort.regist_batch(repository.create, estate_list)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()


@command.register(CreateCompany)
def execute_command_create_company(comando: CreateCompany):
    handler = CreateCompanyHandler()
    handler.handle(comando)


