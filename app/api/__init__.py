import os
from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger
from config import Setting

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    pass

def importar_modelos_alchemy():
    import app.moduls.companies.infrastructure.dto
    

def comenzar_consumidor(app):
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """


    import app.moduls.companies.infrastructure.consumers as list_consumer   
    import threading

# Suscripción a eventos


# Suscripción a comandos
    threading.Thread(target=list_consumer.suscribirse_a_comandos, args=[app]).start()
    threading.Thread(target=list_consumer.suscribirse_a_comandos_delete, args=[app]).start()
    
    
def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = Setting.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from app.config.db import init_db
    init_db(app)

    from app.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        #if not app.config.get('TESTING'):
        comenzar_consumidor(app)

     # Importa Blueprints
    from . import company_router

    app.register_blueprint(company_router.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
