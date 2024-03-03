"""Entidades del dominio de lists

En este archivo usted encontrará las entidades del dominio de lists
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import uuid
from app.moduls .companies.domain.events import CreatedCompany
import app.moduls.lists.domain.value_objects as ov
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class KeyContacts(Entity):    
    name: str = field(default_factory=str)


@dataclass
class Company(RootAggregation):    
    name: str = field(default_factory=str)
    location: str = field(default_factory=str)
    type: str = field(default_factory=str)
    
    def create_company(self, company: Company):
        self.id = company.id
        self.name = company.name
        self.location = company.location
        self.type = company.type

        self.add_events(CreatedCompany(id=self.id, name=self.name, location=self.location, type=self.type))



