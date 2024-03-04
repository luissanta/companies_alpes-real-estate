from __future__ import annotations
from dataclasses import dataclass, field
from app.seedwork.domain.events import (DomainEvent)
# from datetime import datetime

@dataclass
class CreatedCompany(DomainEvent):
    name: str = None
    location: str = None
    typeCompany: str = None

    