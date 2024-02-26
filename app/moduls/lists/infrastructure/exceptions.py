""" Excepciones para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los Excepciones relacionadas
a la capa de infraestructura del dominio de vuelos

"""

#from aeroalpes.seedwork.dominio.excepciones import ExcepcionFabrica
from app.seedwork.domain.exceptions import BusinessRuleException, FactoryException

class NotImplementTypeInFactoryException(BusinessRuleException):
    def __init__(self, mensaje='No existe una implementación para el repositorio con el tipo dado.'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)

class NotImplementDataBaseInFactoryException(FactoryException):
    def __init__(self, mensaje='No existe una implementación para el repositorio con el tipo dado.'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)