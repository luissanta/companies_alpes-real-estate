from pydispatch import dispatcher

from .handlers import HandlerCompanyIntegration

from app.moduls.companies.domain.events import CreatedCompany

dispatcher.connect(HandlerCompanyIntegration.handle_company_created, signal=f'{CreatedCompany.__name__}Integracion')
# dispatcher.connect(HandlerReservaIntegracion.handle_reserva_cancelada, signal=f'{ReservaCancelada.__name__}Integracion')
# dispatcher.connect(HandlerReservaIntegracion.handle_reserva_pagada, signal=f'{ReservaPagada.__name__}Integracion')
# dispatcher.connect(HandlerReservaIntegracion.handle_reserva_aprobada, signal=f'{ReservaAprobada.__name__}Integracion')