
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Name:
    name: str


@dataclass(frozen=True)
class location:
    code: str
   
@dataclass(frozen=True)
class type:
    code: str    