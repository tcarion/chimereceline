import pytest

from chimereceline.stations import Station
from chimereceline.utils import read_stations


def test_station_create():
    stations = read_stations()
    station_data = stations[0]
    station = Station.from_dict(station_data)

    assert station.label == station_data["properties"]["label"]
