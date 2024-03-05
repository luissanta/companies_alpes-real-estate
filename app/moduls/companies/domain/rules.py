from app.seedwork.domain.rules import BusinessRule
from .entities import Company


class CompanyMinOne(BusinessRule):

    company: Company

    def __init__(self, company, mensaje='Los campos name, location y type son obligatorios'):
        super().__init__(mensaje)
        self.company = company

    def is_valid(self) -> bool:
        if not (self.company.name and self.company.type and self.company.location):       
            return True
        return False
