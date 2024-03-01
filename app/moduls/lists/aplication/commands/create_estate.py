from app.seedwork.aplication.commands import Command
from app.moduls.lists.aplication.dto import EstateDTO
from .base import CreateEstateBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplication.commands import execute_command as command

from app.moduls.lists.domain.entities import Estate
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.moduls.lists.aplication.mappers import MapeadorEstate
from app.moduls.lists.infrastructure.repositories import ListRepository

@dataclass
class CreateEstate(Command):
    id: int
    code: str
    name: str
    #estates: list[EstateDTO]


class CreateEstateHandler(CreateEstateBaseHandler):
    
    def handle(self, command: CreateEstate):
        estate_dto = EstateDTO(
                id=command.id
            ,   code=command.code
            ,   name=command.name)
            #,   itinerarios=comando.itinerarios)
        
        estate_list: Estate = self.list_factories.create_object(estate_dto, MapeadorEstate())
        estate_list.create_estate(estate_list)
        repository = self.repository_factory.create_object(ListRepository.__class__)
        print('Llegó instancia del repositorio')

        UnitOfWorkPort.regist_batch(repository.create, estate_list)
        print('Registró batch')
        UnitOfWorkPort.savepoint()
        print('Registró savepoint')
        UnitOfWorkPort.commit()
        print('Realizó commit')


@command.register(CreateEstate)
def execute_command_create_state(comando: CreateEstate):
    handler = CreateEstateHandler()
    handler.handle(comando)
    