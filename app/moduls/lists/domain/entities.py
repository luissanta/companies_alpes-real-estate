"""Entidades del dominio de lists

En este archivo usted encontrará las entidades del dominio de vuelos
"""

from __future__ import annotations
from dataclasses import dataclass, field
import app.moduls.lists.domain.value_objects as ov
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class Estate(Entity):
    code: ov.Code = field(default_factory=ov.Code)
    name: ov.Name = field(default_factory=ov.Name)


@dataclass
class List(RootAggregation):
    estate_id: int = field(hash=True, default=None)
    code: ov.Code = field(default_factory=ov.Code)
    name: ov.Name = field(default_factory=ov.Name)
