from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.lists.domain.entities import Estate, List_estates
from app.moduls.lists.domain.value_objects import Code, Name
from .dto import Estate as EstateDTO ,List_estates as List_estatesDTO

from datetime import datetime
class MapeadorEstate(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def _procesar_estates(self, list_estate: List_estates) -> EstateDTO:
        #EstateDTO(estate_dto.id, estate_dto.code, estate_dto.name)
        return [EstateDTO(id=item.id, code=item.code, name=item.name) for item in list_estate]
    
    
    def _procesar_estates_dto(self, list_estate_dto: List_estatesDTO) -> Estate:
        #Estate(estate_dto.id, estate_dto.code, estate_dto.name)
        return [Estate(id=item.id, code=item.code, name=item.name) for item in list_estate_dto]

    def get_type(self) -> type:
        return List_estates.__class__

    def entity_to_dto(self, list_entidad: List_estates) -> List_estatesDTO:
        if not list_entidad:
            return []
        
        list_dto = List_estates()
        list_dto.estates = list()

        estates: list[Estate] = list_entidad.estates

        list_dto.estates.extend(self._procesar_estates(estates))

        #for estates_entity in enumerate(list_entidad.estates):
        #    estate_dto = EstateDTO(id=estates_entity.id, name=estates_entity.name, code=estates_entity.code)
        #list_dto.estates.append(estate_dto)

        return list_dto

    def dto_to_entity(self, dto: List_estatesDTO) -> List_estates:
        list_estates = List_estates()
        list_estates.estates = list()
        if not dto:
            return list_estates

        

        estates_dto: list[EstateDTO] = dto.estates

        list_estates.estates.extend(self._procesar_estates_dto(estates_dto))

        #estates_map = dto.estates
        #for estat in estates_map:
        #    estate_entity = self._procesar_estates(estat)
        #list_estates.estates.append(estate_entity) 
                
        return list_estates