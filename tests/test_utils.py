import pytest

from chimereceline.constants import API_SOS_URL
from chimereceline.utils import (
    _req_get,
    read_phenomena,
    read_stations,
    retrieve_phenomena,
    retrieve_stations,
    retrieve_timeserie_data,
    retrieve_timeseries,
)


def test_retrieve_stations():
    with pytest.raises(Exception):
        _req_get(API_SOS_URL + "/foo")

    web_stations = retrieve_stations()
    file_stations = read_stations()

    assert web_stations == file_stations, (
        "The saved stations are different than the API ones"
    )


def test_retrieve_phenomena():
    web_phenomena = retrieve_phenomena()
    file_phenomena = read_phenomena()

    assert web_phenomena == file_phenomena, (
        "The saved phenomena are different than the API ones"
    )


def test_retrieve_timeseries():
    ts = retrieve_timeseries(1202, 391)
    assert len(ts) == 1

    id = ts[0]["id"]
    data = retrieve_timeserie_data(id)
    assert len(data) == 1, "The timeseries data could not be properly retrieved"


# import json
# with open('resources/stations.json', 'w') as f:
#     json.dump(stations, f)
