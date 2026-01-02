from dataclasses import dataclass
from typing import Optional


@dataclass
class Coordinates:
  lon: float
  lat: float
  alt: Optional[float] = None
