from dataclasses import dataclass, field
from app.seedwork.aplication.dto import DTO

@dataclass(frozen=True)
class CompanyDTO(DTO):
    name: str = field(default_factory=str)
    location: str = field(default_factory=str) 
    typeCompany: str = field(default_factory=str) 
    
@dataclass(frozen=True)
class ListCompanyDTO(DTO):
    id: str = field(default_factory=str)
    companies: list[CompanyDTO] = field(default_factory=list[CompanyDTO])


