
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Name:
    name: str


@dataclass(frozen=True)
class Location:
    code: str
   
@dataclass(frozen=True)
class Type:
    code: str    