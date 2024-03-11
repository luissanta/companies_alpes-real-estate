import json
import uuid
from flask import Flask
from app.moduls.companies.aplication.commands.create_company import CreateCompany
from app.moduls.companies.aplication.commands.delete_company import DeleteCompany
from app.moduls.companies.infrastructure.dispachers import Despachador
from app.moduls.companies.infrastructure.dto import Company
from app.moduls.companies.infrastructure.schema.v1.commands import CommandResponseCreateCompanyJson, CommandResponseRollbackCreateCompanyJson
from app.seedwork.aplication.commands import execute_command
from app.seedwork.infrastructure import utils
import pulsar,_pulsar  
from pulsar.schema import *

from app.config.db import db    
def suscribirse_a_comandos(app):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('create-company', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            mensaje = consumer.receive()
            #print("Mensaje recibido: {}".format(mensaje.data().decode('utf-8')))
            with app.test_request_context():
                command = CreateCompany(str(uuid.uuid4()),"uniandes","uniandes","uniandes")   
                execute_command(command)

                despachador = Despachador()
                command = CommandResponseCreateCompanyJson()
                
                command.data = "OK"               
                despachador.publicar_comando_respuesta(command, 'response-create-company')

            consumer.acknowledge(mensaje)
    except Exception as e:
        despachador = Despachador()
        command = CommandResponseRollbackCreateCompanyJson()
        command.data = str(-1)
        despachador.publicar_comando_rollback(command, 'response-rollback-create-company')
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
    finally:
        if client:
            client.close()


def suscribirse_a_comandos_delete(app):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('delete-company', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Mensaje recibido: {}".format(mensaje.data().decode('utf-8')))
            with app.test_request_context():
                print(f"Current app name: {app.name}")
                json_data = json.loads(mensaje.data().decode('utf-8'))

                command = DeleteCompany(-1)   
                execute_command(command)

                despachador = Despachador()
                command = CommandResponseRollbackCreateCompanyJson()

                command.data = str(-1)
                despachador.publicar_comando_rollback(command, 'response-rollback-create-company')

            consumer.acknowledge(mensaje)

        client.close()
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
    finally:
        if client:
            client.close()
