""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""


#from aeroalpes.modulos.vuelos.dominio.repositorios import RepositorioReservas, RepositorioProveedores
#from aeroalpes.modulos.vuelos.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
#from aeroalpes.modulos.vuelos.dominio.entidades import Proveedor, Aeropuerto, Reserva
#from aeroalpes.modulos.vuelos.dominio.fabricas import FabricaVuelos
#from .dto import Reserva as ReservaDTO
#from .mapeadores import MapeadorReserva
from app.config.db import get_db, engine, SessionLocal
from .dto import Listado as ListadoDTO
from uuid import UUID
from app.moduls.lists.domain.entities import List
from app.moduls.lists.domain.repositories import RepositorioListado


class RepositorioPropiedadesSQLite(RepositorioListado):

    def obtener_por_id(self, id: UUID) -> List:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[List]:
        session = SessionLocal()
        reserva_dto = session.query(ListadoDTO).all()
        #Quiero crear un mapeador del objeto ListDTO al objeto List
        estate_list = [List(id=item.id, code=item.code, name=item.name) for item in reserva_dto]


        #falta mapear Revisar.........
        #temp = len(reserva_dto)
        #estate_list = List(id=1,estate_id=temp, code="1", name="List 1")
        return [estate_list]

    def agregar(self, entity: List):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: List):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError