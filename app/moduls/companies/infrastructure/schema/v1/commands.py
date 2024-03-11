from pulsar.schema import *
from dataclasses import dataclass, field
from app.seedwork.infrastructure.schema.v1.comandos import (ComandoIntegracion)
from app.seedwork.infrastructure.schema.v1.mensajes import Mensaje

class ComandoCrearReservaPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearReserva(ComandoIntegracion):
    data = ComandoCrearReservaPayload()

class EventoIntegracion1(Mensaje):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommandResponseCreateAuditJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommandResponseCreateCompanyJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# class CommandResponseCreateCompanyJson(Record):
#     data = String()

class CommandResponseRollbackCreateCompanyJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)