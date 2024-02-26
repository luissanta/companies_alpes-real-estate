"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from app.seedwork.domain.rules import BusinessRule
from .value_objects import Name, Code
from .entities import Estate


class MinimoUnaPropiedad(BusinessRule):

    estates: list[Estate]

    def __init__(self, estates, mensaje='Al menos una propiedad debe estar en el listado'):
        super().__init__(mensaje)
        self.estates = estates

    def es_valido(self) -> bool:
        for estates in self.estates:
            if estates.code == Estate.code:
                return True
        return False

# class RutaValida(ReglaNegocio):

#     ruta: Ruta

#     def __init__(self, ruta, mensaje='La ruta propuesta es incorrecta'):
#         super().__init__(mensaje)
#         self.ruta = ruta

#     def es_valido(self) -> bool:
#         return self.ruta.destino != self.ruta.origen

# class MinimoUnItinerario(ReglaNegocio):
#     itinerarios: list[Itinerario]

#     def __init__(self, itinerarios, mensaje='La lista de itinerarios debe tener al menos un itinerario'):
#         super().__init__(mensaje)
#         self.itinerarios = itinerarios

#     def es_valido(self) -> bool:
#         return len(self.itinerarios) > 0 and isinstance(self.itinerarios[0], Itinerario) 