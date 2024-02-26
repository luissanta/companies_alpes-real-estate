""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from app.moduls.lists.domain.exceptions import TipoObjetoNoExisteEnDominioPropiedadesExcepcion

from app.moduls.lists.domain.rules import MinimoUnaPropiedad
from app.seedwork.domain.repositories import Mapper
from .entities import Estate, Entity
#from .reglas import MinimoUnItinerario, RutaValida
#from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
#from aeroalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
#from aeroalpes.seedwork.dominio.fabricas import Fabrica
#from aeroalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass
from app.seedwork.domain.factories import Factory

@dataclass
class _FabricaListado(Factory):
    def crear_objeto(self, obj: any, mapeador: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapeador.entidad_a_dto(obj)
        else:
            reserva: list = mapeador.dto_a_entidad(obj)

            self.validar_regla(MinimoUnaPropiedad(Estate.code))
                       
            return reserva

@dataclass
class FabricaListados(Factory):
    def crear_objeto(self, obj: any, mapeador: Mapper) -> any:
        if mapeador.obtener_tipo() == Estate.__class__:
            fabrica_reserva = _FabricaListado()
            return fabrica_reserva.build_object(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion()