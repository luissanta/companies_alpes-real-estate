import json
import uuid
from flask import Flask
from app.moduls.companies.infrastructure.dispachers import Despachador
from app.moduls.companies.infrastructure.dto import Company
from app.moduls.companies.infrastructure.schema.v1.commands import CommandResponseCreateCompanyJson, CommandResponseRollbackCreateCompanyJson
from app.seedwork.infrastructure import utils
import pulsar,_pulsar  
from pulsar.schema import *
from app.config.db import init_db
from config import Setting
import app.moduls.companies.infrastructure.dto

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = Setting.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
app.config['SESSION_TYPE'] = 'filesystem'
init_db(app)
from app.config.db import db    
def suscribirse_a_comandos():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('create-company', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Mensaje recibido: {}".format(mensaje.data().decode('utf-8')))
            with app.app_context():
                db.create_all()
                print(f"Current app name: {app.name}")
                entity = Company()
                entity.id = str(uuid.uuid4())
                entity.name = "name"
                entity.location = "name"
                entity.typeCompany = "name"
                entity_id_json = json.dumps({"id": entity.id})
                db.session.add(entity)
                db.session.commit()
                db.session.close()

                despachador = Despachador()
                command = CommandResponseCreateCompanyJson()
                
                command.data = entity_id_json               
                despachador.publicar_comando(command, 'response-create-company')

                #Intento con Repository
                # repository_factory = RepositoryFactory()
                # repository = repository_factory.create_object(CompanyRepository.__class__)   
                # repository.create(entity)

                #Intento con Comandos
                # command = CreateCompany(entity.id,entity.location,entity.name,entity.typeCompany)   
                # execute_command(command)
                # repository = CompanyRepositoryPostgres()

            consumer.acknowledge(mensaje)

        client.close()
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
    finally:
        if client:
            client.close()


def suscribirse_a_comandos_delete():
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('delete-company', consumer_type=pulsar.ConsumerType.Shared,
                                    subscription_name='audit-sub-commands')

        while True:
            mensaje = consumer.receive()
            print("Mensaje recibido: {}".format(mensaje.data().decode('utf-8')))
            with app.app_context():
                db.create_all()
                print(f"Current app name: {app.name}")
                json_data = json.loads(mensaje.data().decode('utf-8'))
                id_value = json_data.get("id")

                db.session.query(Company).filter(Company.id == id_value).delete()
                db.session.commit()
                db.session.close()

                despachador = Despachador()
                command = CommandResponseRollbackCreateCompanyJson()
                
                command.data = id_value               
                despachador.publicar_comando(command, 'response-rollback-create-company')

            consumer.acknowledge(mensaje)

        client.close()
    except Exception as e:
        print(e)
        print('ERROR: Suscribiendose al tópico de comandos!')
    finally:
        if client:
            client.close()
