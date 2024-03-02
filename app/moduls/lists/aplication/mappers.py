from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.lists.domain.entities import Estate, List_estates
from app.moduls.lists.domain.value_objects import Code, Name
from .dto import EstateDTO, ListDTO

from datetime import datetime

class MapeadorEstateDTOJson(AppMap):
    def _procesar_estate(self, estate: dict) -> EstateDTO:

        estate_dto: EstateDTO = EstateDTO(estate.get('id'), estate.get('code'), estate.get('name')) 
        return estate_dto
    
    def external_to_dto(self, externo: dict) -> ListDTO:

        list_dto = ListDTO()

        estates: list[EstateDTO] = list()
        for itin in externo:
            list_dto.estates.append(self._procesar_estate(itin))

        return list_dto

    def dto_to_external(self, dto: EstateDTO) -> dict:
        return dto.__dict__

class MapeadorEstate(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def _procesar_estates(self, estate_dto: EstateDTO) -> Estate:
        return Estate(estate_dto.id, estate_dto.code, estate_dto.name)

    def get_type(self) -> type:
        return Estate.__class__

    def entity_to_dto(self, list_entidad: List_estates) -> ListDTO:
        list_dto = ListDTO()

        for estates_entity in list_entidad.estates:
            estate_dto = EstateDTO(id=estates_entity.id, name=estates_entity.name, code=estates_entity.code)
            list_dto.estates.append(estate_dto) 

        return list_dto

    def dto_to_entity(self, dto: ListDTO) -> List_estates:
        list_estates = List_estates(id=1)
        list_estates.estates = list()

        estates_map = dto.estates
        for estat in estates_map:
            estate_entity = self._procesar_estates(estat)
            list_estates.estates.append(estate_entity) 
            
        return list_estates
    

    # def dto_a_entidad(self, dto: ReservaDTO) -> Reserva:
    #     reserva = Reserva()
    #     reserva.itinerarios = list()

    #     itinerarios_dto: list[ItinerarioDTO] = dto.itinerarios

    #     for itin in itinerarios_dto:
    #         reserva.itinerarios.append(self._procesar_itinerario(itin))
        
    #     return reserva

    # def dto_a_entidad(self, dto: ReservaDTO) -> Reserva:
    #     reserva = Reserva()
    #     reserva.itinerarios = list()

    #     itinerarios_dto: list[ItinerarioDTO] = dto.itinerarios

    #     for itin in itinerarios_dto:
    #         reserva.itinerarios.append(self._procesar_itinerario(itin))
        
    #     return reserva
