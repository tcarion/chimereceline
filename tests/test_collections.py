import pytest

from chimereceline.collection import SosCollection
from chimereceline.stations import Station, generate_stations
from chimereceline.utils import read_stations


def test_station_create():
    stations_data = read_stations()
    station_data = stations_data[0]
    station = Station.from_dict(station_data)

    assert station.label == station_data["properties"]["label"]

    stations = generate_stations()
    assert stations[0] == station

    label = station.label
    assert label == station.code + " - " + station.location_name


def test_collection():
    coll = SosCollection()
    assert coll.search_station("Houtem")[0].id == 1202
    assert coll.search_phenomenon("Black Carbon")[0].id == 391
