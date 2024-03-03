from app.moduls.companies.domain.events import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from app.seedwork.aplication.handlers import Handler
from app.moduls.companies.infrastructure.dispachers import Despachador

class HandlerCompanyIntegration(Handler):

    @staticmethod
    def handle_company_created(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'events-company')

    # @staticmethod
    # def handle_reserva_cancelada(evento):
    #     despachador = Despachador()
    #     despachador.publicar_evento(evento, 'eventos-reserva')

    # @staticmethod
    # def handle_reserva_aprobada(evento):
    #     despachador = Despachador()
    #     despachador.publicar_evento(evento, 'eventos-reserva')

    # @staticmethod
    # def handle_reserva_pagada(evento):
    #     despachador = Despachador()
    #     despachador.publicar_evento(evento, 'eventos-reserva')


    