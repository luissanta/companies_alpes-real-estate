""" Fábricas para la creación de objetos reusables parte del seedwork del proyecto

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos reusables parte del seedwork del proyecto

"""

from abc import ABC, abstractmethod
from .repositories import Mapper
from .mixins import ValidateRulesMixin

class Factory(ABC, ValidateRulesMixin):
    @abstractmethod
    def crear_objeto(self, obj: any, mapper: Mapper=None) -> any:
        ...
