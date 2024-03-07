import app.seedwork.presentation.apiflask as apiflask
import json
from typing import Any, Dict
from flask import redirect, render_template, request, session, url_for
from flask import Response, Request



from app.moduls.companies.aplication.service import CompanyService
from app.moduls.companies.aplication.mappers import MapeadorCompanyDTOJson as MapApp
from app.moduls.companies.aplication.commands.create_company import CreateCompany
from app.moduls.companies.aplication.commands.delete_company import DeleteCompany
from app.seedwork.domain.exceptions import DomainException
from app.moduls.companies.aplication.service import CompanyService
from app.seedwork.aplication.commands import execute_command
from app.seedwork.aplication.queries import execute_query

bp = apiflask.create_blueprint('company_router', '/company_router')

@bp.route("/company", methods=('GET',)) 
def get_list():
    map_estates = MapApp()
    sr = CompanyService()
    return map_estates.dto_to_external(sr.get_all_list())

# @bp.route("/listQuery", methods=('GET',))
# def get_estate_using_query(id=None):
#     query_resultado = execute_query(GetEstate(id))
#     map_estates = MapApp()
    
#     return map_estates.dto_to_external(query_resultado.resultado)

@bp.route("/company-command", methods=('POST',))
def async_create_state():
    try:
        estate_dict = request.json
       
        map_estate = MapApp()
        compamy_dto = map_estate.external_to_dto(estate_dict)

        command = CreateCompany(compamy_dto.id,compamy_dto.location,compamy_dto.name,compamy_dto.typeCompany)   
        
     
        execute_command(command)
        
        return Response('{}', status=201, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route("/company-command/<uuid:id>", methods=['DELETE'])
def delete_item(id):
    try:
        command = DeleteCompany(id)       
        execute_command(command)
        
        return Response('{}', status=204, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')