#from aeroalpes.seedwork.aplicacion.servicios import Servicio
#from aeroalpes.modulos.vuelos.dominio.entidades import Reserva
#from aeroalpes.modulos.vuelos.dominio.fabricas import FabricaVuelos
#from aeroalpes.modulos.vuelos.infraestructura.fabricas import FabricaRepositorio
#from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioReservas
#from .mapeadores import MapeadorReserva

#from .dto import ReservaDTO

from .dto import ListDTO
from app.moduls.lists.domain.factories import FabricaListados
from app.moduls.lists.infrastructure.factories import RepositoryFactory
from app.seedwork.aplication.services import Servicio
from app.moduls.lists.infrastructure.repositories import RepositorioListado

class ServicioListado(Servicio):

    def __init__(self):
        self._fabrica_repositorio: RepositoryFactory = RepositoryFactory()
        self._fabrica_listados: FabricaListados = FabricaListados()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_listados(self):
        return self._fabrica_listados

    def obtener_listado_por_id(self, id) -> ListDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioListado.__class__)
        return repositorio.obtener_todos()#.__dict__
    