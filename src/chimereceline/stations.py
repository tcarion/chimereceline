import re
from dataclasses import dataclass
from typing import Any, Dict, List, Literal

from chimereceline.utils import read_stations

label_pattern = r"^(.{6})\s*-\s*(.+)$"


@dataclass(frozen=True)
class Station:
    lon: float
    lat: float
    height: float | None
    id: int
    label: str
    location_name: str | Literal[""]
    code: str | Literal[""]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Station":
        """Factory method to create a Station from the given dictionary."""
        properties = data["properties"]
        coordinates = data["geometry"]["coordinates"]
        label = properties["label"]
        m = re.match(label_pattern, label)
        code, location_name = m.groups() if m is not None else ("", "")

        return cls(
            lon=coordinates[0],
            lat=coordinates[1],
            height=float(coordinates[2]) if coordinates[2] != "NaN" else None,
            id=int(properties["id"]),
            label=label,
            location_name=location_name,
            code=code,
        )


def generate_stations() -> List[Station]:
    return [Station.from_dict(station) for station in read_stations()]
