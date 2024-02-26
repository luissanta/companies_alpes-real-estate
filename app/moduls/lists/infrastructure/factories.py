""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from app.moduls.lists.domain.repositories import RepositorioListado
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repositorio
from .repositories import RepositorioPropiedadesSQLite
from .exceptions import FactoryException
@dataclass
class RepositoryFactory(Factory):
    def crear_objeto(self, obj: type, mapper: any = None) -> Repositorio:
        if obj == RepositorioListado.__class__:
            return RepositorioPropiedadesSQLite()
        else:
            raise FactoryException()