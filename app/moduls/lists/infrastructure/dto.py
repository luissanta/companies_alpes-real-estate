"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos
"""

from app.config.db import db
from sqlalchemy import Column, String

Base = db.declarative_base()
class Estate(db.Model):
    __tablename__ = "estatelist"
    id = db.Column(db.String, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)