from app.seedwork.aplication.queries import Query, QueryHandler, QueryResultado
from app.seedwork.aplication.queries import ejecutar_query as query
from app.moduls.lists.infrastructure.repositories import ListRepository
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from app.moduls.lists.aplication.mappers import MapeadorEstate
import uuid

@dataclass
class ObtenerReserva(Query):
    id: str

class getEstatesHandler(ReservaQueryBaseHandler):
    def handle(self, query: ObtenerReserva) -> QueryResultado:
        repositorio = self._repository_factory.create_object(ListRepository.__class__)
        reserva =  self._list_factories.create_object(repositorio.obtener_por_id(query.id), MapeadorEstate())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerReserva)
def ejecutar_query_obtener_reserva(query: ObtenerReserva):
    handler = getEstatesHandler()
    return handler.handle(query)