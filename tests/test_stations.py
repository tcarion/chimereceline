import pytest

from chimereceline.stations import Station, generate_stations
from chimereceline.utils import read_stations


def test_station_create():
    stations_data = read_stations()
    station_data = stations_data[0]
    station = Station.from_dict(station_data)

    assert station.label == station_data["properties"]["label"]

    stations = generate_stations()
    assert stations[0] == station
