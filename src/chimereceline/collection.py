from dataclasses import dataclass

from chimereceline.phenomena import generate_phenomena
from chimereceline.stations import generate_stations


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
