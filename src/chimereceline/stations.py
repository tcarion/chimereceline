from dataclasses import dataclass
from typing import Any, Dict, List

from chimereceline.utils import read_stations


@dataclass(frozen=True)
class Station:
    lon: float
    lat: float
    height: float | None
    id: int
    label: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Station":
        """Factory method to create a Station from the given dictionary."""
        properties = data["properties"]
        coordinates = data["geometry"]["coordinates"]

        return cls(
            lon=coordinates[0],
            lat=coordinates[1],
            height=float(coordinates[2]) if coordinates[2] != "NaN" else None,
            id=properties["id"],
            label=properties["label"],
        )


def generate_stations() -> List[Station]:
    return [Station.from_dict(station) for station in read_stations()]
