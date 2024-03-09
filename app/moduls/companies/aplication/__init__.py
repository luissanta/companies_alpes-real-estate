from pydispatch import dispatcher

from .handlers import HandlerCompanyIntegration

from app.moduls.companies.infrastructure.schema.v1.commands  import CommandResponseCreateCompanyJson

dispatcher.connect(HandlerCompanyIntegration.handle_company_created, signal=f'{CommandResponseCreateCompanyJson.__name__}Integracion')
# dispatcher.connect(HandlerReservaIntegracion.handle_reserva_cancelada, signal=f'{ReservaCancelada.__name__}Integracion')
# dispatcher.connect(HandlerReservaIntegracion.handle_reserva_pagada, signal=f'{ReservaPagada.__name__}Integracion')
# dispatcher.connect(HandlerReservaIntegracion.handle_reserva_aprobada, signal=f'{ReservaAprobada.__name__}Integracion')

