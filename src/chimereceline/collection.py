from dataclasses import dataclass
from typing import List, Literal

from chimereceline.phenomena import Phenomenon, generate_phenomena
from chimereceline.stations import Station, generate_stations


@dataclass(frozen=True)
class SosCollection:
    stations = generate_stations()
    phenomena = generate_phenomena()

    def search_phenomenon(self, name: str):
        matches = [p for p in self.phenomena if name in p.label]
        return matches

    def search_station(self, name: str):
        matches = [s for s in self.stations if name in s.location_name]
        return matches

    def get_by_id(self, id: int, type: Literal["Station"] | Literal["Phenomenon"]):
        tosearch: List[Station] | List[Phenomenon] | None = None
        if type == "Station":
            tosearch = self.stations
        elif type == "Phenomenon":
            tosearch = self.phenomena
        else:
            raise RuntimeError(f"Wrong collection type: {type}.")

        match = [e for e in tosearch if id == e.id]
        if len(match) != 1:
            RuntimeError(f"ID: {id} could not be found.")

        return match[0]
