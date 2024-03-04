from app.config.db import db
from sqlalchemy import Column, String

Base = db.declarative_base()

list_company_company = db.Table(
    "list_company_company",
    db.Model.metadata,
    db.Column("id", db.String, db.ForeignKey("list_company.id")),
    db.Column("company_id", db.String),
    db.Column("name", db.String),
    db.Column("localtion", db.String),
    db.Column("typeCompany", db.String),
    db.ForeignKeyConstraint(
        ["company_id", "name", "localtion","typeCompany"],
        ["company.company_id", "company.name", "company.location","company.typeCompany"]
    )
)

class Company(db.Model):
    __tablename__ = "company"
    company_id = db.Column(db.String, primary_key=True)  
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    typeCompany = db.Column(db.String, nullable=False)    

    
class List_company(db.Model):
    __tablename__ = "list_company"
    id = db.Column(db.String, primary_key=True)    
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
    companies = db.relationship('Company', secondary=list_company_company, backref='list_company')        
       
    
