""" Interfaces para los repositorios reusables parte del seedwork del proyecto

En este archivo usted encontrará las diferentes interfaces para repositorios
reusables parte del seedwork del proyecto
"""

from abc import ABC, abstractmethod
from uuid import UUID
from .entities import Entity

class Repositorio(ABC):
    @abstractmethod
    def obtener_por_id(self, id: UUID) -> Entity:
        ...

    @abstractmethod
    def obtener_todos(self) -> list[Entity]:
        ...

    @abstractmethod
    def agregar(self, entity: Entity):
        ...

    @abstractmethod
    def actualizar(self, entity: Entity):
        ...

    @abstractmethod
    def eliminar(self, entity_id: UUID):
        ...


class Mapper(ABC):
    @abstractmethod
    def obtener_tipo(self) -> type:
        ...

    @abstractmethod
    def entidad_a_dto(self, entidad: Entity) -> any:
        ...

    @abstractmethod
    def dto_a_entidad(self, dto: any) -> Entity:
        ...