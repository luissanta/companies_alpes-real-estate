from dataclasses import dataclass, field
from app.seedwork.aplication.dto import DTO

@dataclass(frozen=True)
class CompanyDTO(DTO):
    name: str = field(default_factory=str)
    ubication: str = field(default_factory=str) 
    type: str = field(default_factory=str) 


