import json
import pulsar
from pulsar.schema import *


from app.moduls.companies.infrastructure.schema.v1.commands import ComandoCrearReserva, ComandoCrearReservaPayload, CommandResponseCreateCompanyJson, CommandResponseRollbackCreateCompanyJson
from app.seedwork.infrastructure import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoCrearReservaPayload))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico)
        serialized_data = json.dumps(evento.data).encode('utf-8')       
        publicador.send(serialized_data)
        publicador.close()

    def publicar_comando(self, comando, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico)
        serialized_data = json.dumps(comando.data).encode('utf-8')       
        publicador.send(serialized_data)
        publicador.close()

    def publicar_comando_respuesta(self, comando, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(CommandResponseCreateCompanyJson)  )  
        publicador.send(comando)
        publicador.close()

    def publicar_comando_rollback(self, comando, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(CommandResponseRollbackCreateCompanyJson))     
        publicador.send(comando)
        publicador.close()