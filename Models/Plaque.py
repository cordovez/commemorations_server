""" Data Classes """
from dataclasses import dataclass
from typing import Dict, Optional


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

    original_id: int
    original_record: str
    commemorates: Commemoration
    street_address: Optional[str] | None = None
    arrondissement: Optional[int] | None = None
    city: Optional[str] | None = None
    address_complement: Optional[str] | None = None
    coordinates: Optional[Coordinates] | None = None


@dataclass
class PlaqueUpdates:
    """Plaque with Coordinates and Commemoration descendants"""

    commemorates: Optional[Commemoration] | None = None
    street_address: Optional[str] | None = None
    arrondissement: Optional[int] | None = None
    address_complement: Optional[str] | None = None
    coordinates: Optional[Coordinates] | None = None
