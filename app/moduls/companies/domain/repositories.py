from abc import ABC
from app.seedwork.domain.repositories import Repository


class CompanyRepository(Repository, ABC):
    ...