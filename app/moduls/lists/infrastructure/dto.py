"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""


from app.config.db import Base, engine
from sqlalchemy import Column, ForeignKey, Integer, Table,String

import uuid



# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios

class Listado(Base):
    __tablename__ = "listado"
    id = Column(String, primary_key=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)


#Base.metadata.create_all(get_db.engine)
Base.metadata.create_all(bind=engine)