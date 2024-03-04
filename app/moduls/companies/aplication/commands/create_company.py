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
class CreateCompany(Command):
    id: str
    name: str
    location: str
    typeCompany: str
    

class CreateCompanyHandler(CreateCompanyBaseHandler):
    
    def handle(self, command: CreateCompany):
        company = command
        # company_dto = CompanyDTO(id=str(company.id), name=company.name, location=company.location, typeCompany=company.typeCompany)

        
        company: Company = self.list_factories.create_object(company, MapeadorCompany())
        company.create_company(company)
        repository = self.repository_factory.create_object(CompanyRepository.__class__)

        UnitOfWorkPort.regist_batch(repository.create, company)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()


@command.register(CreateCompany)
def execute_command_create_company(comando: CreateCompany):
    handler = CreateCompanyHandler()
    handler.handle(comando)


