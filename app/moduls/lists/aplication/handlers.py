# from app.moduls.lists.domain.events import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
# from app.seedwork.aplication.handlers import Handler
# from app.moduls.lists.infrastructure.despachadores import Despachador

# class HandlerReservaIntegracion(Handler):

#     @staticmethod
#     def handle_created_es(evento):
#         despachador = Despachador()
#         despachador.publicar_evento(evento, 'eventos-reserva')

#     @staticmethod
#     def handle_reserva_cancelada(evento):
#         despachador = Despachador()
#         despachador.publicar_evento(evento, 'eventos-reserva')

#     @staticmethod
#     def handle_reserva_aprobada(evento):
#         despachador = Despachador()
#         despachador.publicar_evento(evento, 'eventos-reserva')

#     @staticmethod
#     def handle_reserva_pagada(evento):
#         despachador = Despachador()
#         despachador.publicar_evento(evento, 'eventos-reserva')