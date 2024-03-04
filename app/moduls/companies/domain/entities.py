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
class Company(Entity):
    location: str = field(default_factory=str)
    name: str = field(default_factory=str)
    typeCompany:str= field(default_factory=str)

@dataclass
class List_Company(RootAggregation):
    id: str = field(hash=True, default=None)
    companies: list[Company] = field(default_factory=list)
    # created_at: datetime = field(default=datetime.now())
    # updated_at: datetime = field(default=datetime.now())

    def create_company(self, companies: List_Company):
       self.companies = companies
    #   self.add_events(CreatedCompany(id=self.id, name=self.name, location=self.location, typeCompany=self.typeCompany))


