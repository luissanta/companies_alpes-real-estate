"""Entidades del dominio de lists

En este archivo usted encontrará las entidades del dominio de lists
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import uuid
from app.moduls .companies.domain.events import CreatedCompany
from app.moduls.companies.infrastructure.schema.v1.commands import CommandResponseCreateCompanyJson
from app.seedwork.domain.entities import Entity, RootAggregation



@dataclass
class Company(RootAggregation):
    id: uuid.UUID = field(hash=True, default=None)
    name: str = field(default_factory=str)
    location:str = field(default_factory=str)
    typeCompany:str = field(default_factory=str)


    def create_company(self, company: Company):
        company = company
        #self.add_events(CommandResponseCreateCompanyJson(data=self.id))

    def delete_company(self,id:any):
        id=id
