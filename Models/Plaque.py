""" Data Classes """
from dataclasses import dataclass
from typing import Optional


@dataclass
class Commemoration:
    """Child of Plaque"""

    other: str
    first_name: Optional[str] | None = None
    last_name: Optional[str] | None = None


@dataclass
class Coordinates:
    """Child of Plaque"""

    lon: float
    lat: float


@dataclass
class Plaque:
    """Plaque with Coordinates and Commemoration descendants"""

    original_id: int
    commemorates: Commemoration
    address: str
    address_complement: str
    arrondissement: int
    coordinates: Coordinates
