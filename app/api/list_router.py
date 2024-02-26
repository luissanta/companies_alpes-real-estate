from fastapi import APIRouter, status

from app.moduls.lists.aplication.services import ServicioListado

list_router = APIRouter(
    tags=["list"]
)


@list_router.get("/list", status_code=status.HTTP_200_OK)
async def get_list():
    sr = ServicioListado()   
    return sr.obtener_listado_por_id(id)
   


#import aeroalpes.seedwork.presentacion.api as api
#import json
#from aeroalpes.modulos.vuelos.aplicacion.servicios import ServicioReserva
#from aeroalpes.modulos.vuelos.aplicacion.dto import ReservaDTO
#from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

#from flask import redirect, render_template, request, session, url_for
#from flask import Response
#from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReservaDTOJson

