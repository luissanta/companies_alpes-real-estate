from app.config.db import db
from sqlalchemy import Column, String

Base = db.declarative_base()

class Company(db.Model):
    __tablename__ = "company" 
    id= db.Column(db.String, primary_key=True)  
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    typeCompany = db.Column(db.String, nullable=False)    

