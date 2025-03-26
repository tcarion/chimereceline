import datetime as dt

from chimereceline.collection import SosCollection
from chimereceline.stations import Station, generate_stations
from chimereceline.timeseries import TimeSerie
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


def test_timeseries():
    coll = SosCollection()
    sta = coll.search_station("Houtem")[0]
    phen = coll.search_phenomenon("Black Carbon")[0]
    ts = TimeSerie(sta, phen)
    assert ts.id == 10606

    start = dt.datetime(2025, 1, 1, 0)
    end = dt.datetime(2025, 1, 1, 5)
    t1, v1 = ts.get_data()
    assert len(v1) == 168

    t2, v2 = ts.get_data(starttime=start, endtime=end)

    assert len(v2) == 6

    # for some reason the actual retrieved times are 1hours before
    assert ts.timespan[0] == start - dt.timedelta(hours=1)
    assert ts.timespan[1] == end - dt.timedelta(hours=1)
