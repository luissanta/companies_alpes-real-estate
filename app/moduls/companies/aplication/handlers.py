# from app.moduls.companies.domain.events import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from app.seedwork.aplication.handlers import Handler
from app.moduls.companies.infrastructure.dispachers import Despachador

class HandlerCompanyIntegration(Handler):

    @staticmethod
    def handle_company_created(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'response-company')
