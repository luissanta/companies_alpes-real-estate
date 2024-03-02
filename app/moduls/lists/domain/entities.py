"""Entidades del dominio de lists

En este archivo usted encontrará las entidades del dominio de lists
"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime
import app.moduls.lists.domain.value_objects as ov
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class Estate(Entity):
    id: int = field(default=None)
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)
    createdAt: str = field(default_factory=str)
    updatedAt: str = field(default_factory=str)

@dataclass
class List_estates(RootAggregation):
    estates: list[Estate] = field(default_factory=list)

    def create_estate(self, estateslist: List_estates):
        estates = estateslist
        # for estate in estateslist:
        #     self.estate.id = estate.id
        #     self.estate.code = estate.code
        #     self.estate.name = estate.name
        #     self.createdAt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        #     self.updatedAt = None #datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        
        #     self.estates.append(estate)