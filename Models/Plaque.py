""" Data Classes """
from dataclasses import dataclass
from typing import Optional


@dataclass
class Commemoration:
    """Child of Plaque"""

    other: Optional[str] | None = None
    first_name: Optional[str] | None = None
    last_name: Optional[str] | None = None


@dataclass
class Coordinates:
    """Child of Plaque"""

    lon: Optional[float] | None = None
    lat: Optional[float] | None = None


@dataclass
class Plaque:
    """Plaque with Coordinates and Commemoration descendants"""

    commemorates: Commemoration
    street_address: str
    arrondissement: int
    city: str
    address_complement: str
    coordinates: Coordinates
    original_id: int
