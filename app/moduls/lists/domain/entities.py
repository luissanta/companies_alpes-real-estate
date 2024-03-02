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
    #createdAt: str = field(default_factory=str)
    #updatedAt: str = field(default_factory=str)

    def create_estate(self, estate: Estate):
        self.id = estate.id
        self.code = estate.code
        self.name = estate.name

@dataclass
class List(RootAggregation):
    #estate_id: int = field(hash=True, default=None)
    #estates: list[Estate] = field(default_factory=list)
    estate: Estate = field(default_factory=Estate)

    def create_estate(self, estate: Estate):
        self.estate.id = estate.id
        self.estate.code = estate.code
        self.estate.name = estate.name
        #self.createdAt = datetime.strftime(datetime.now, '%Y-%m-%d %H:%M:%S')
        #self.updatedAt = None #datetime.strftime(datetime.now, '%Y-%m-%d %H:%M:%S')
        
        
