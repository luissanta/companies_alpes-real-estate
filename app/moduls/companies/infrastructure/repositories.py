from app.config.db import db
from .dto import Company as CompanyDTO
from ..domain.entities import Company

from ..domain.repositories import CompanyRepository
from ..domain.factory import CompanyFactory
from ..infrastructure.mappers import MapeadorCompany
from flask import Response, Request
import json

class CompanyRepositoryPostgres(CompanyRepository):

    def __init__(self):
        self._company_factory: CompanyFactory = CompanyFactory()

    @property
    def companies_factory(self):
        return self._company_factory
    
 
    def get_by_id(self, entity_id: int) -> Company:
        # TODO
        list_estate_dto = db.session.query(
            CompanyDTO).filter_by(id=str(entity_id)).one()
        try:
            estate_list_entity = []
            # self.companies_factory.create_object(
            #     list_estate_dto, MapeadorCompany())
        except Exception as e:
            print("Error: ", e)
        return estate_list_entity

    def get_all(self) -> list[Company]:
        list_estate_dto = db.session.query(CompanyDTO).all()
        estate_list_entity=[]
        try:
            estate_list_entity = self.companies_factory.create_object(list_estate_dto, MapeadorCompany())
            # [Company(id=item.id, name=item.name, location=item.location,typeCompany=item.typeCompany) for item in list_estate_dto]
        except Exception as e:
            print("Error: ", e)

        return estate_list_entity

    def create(self, entity: Company):
        listesates_dto = self.companies_factory.create_object(entity, MapeadorCompany())
        # companyDto= CompanyDTO(id=entity.id, name=entity.name, location=entity.location, typeCompany=entity.typeCompany)
        db.session.add(listesates_dto)

    def update(self, entity_id: int, entity: Company):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: int):       
        try:       
           
            item = db.session.query(CompanyDTO).filter_by(id=str(entity_id)).first()
            estate_list_entity = self.companies_factory.create_object(item, MapeadorCompany())
            if item:   
                     
                db.session.delete(item)
                db.session.commit()
                           
            else:    
                return Response(json.dumps(dict(error='Item not found')), status=404, mimetype='application/json')
        except Exception as e:    
            # db.session.rollback()
            print(str(e))
            # return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')