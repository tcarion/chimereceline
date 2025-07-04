import pytest

from chimereceline.constants import API_SOS_URL
from chimereceline.utils import (
    _make_timeseries_req,
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

    web_stations = retrieve_stations().json()
    file_stations = read_stations()

    assert web_stations == file_stations, (
        "The saved stations are different than the API ones"
    )


def test_retrieve_phenomena():
    web_phenomena = retrieve_phenomena().json()
    file_phenomena = read_phenomena()

    assert web_phenomena == file_phenomena, (
        "The saved phenomena are different than the API ones"
    )


def test_retrieve_timeseries():
    req = _make_timeseries_req(1202, 391)
    response = _req_get(req["url"], params=req["payload"])
    ts = retrieve_timeseries(1202, 391).json()
    assert len(ts) == 1

    id = ts[0]["id"]
    data = retrieve_timeserie_data(id).json()
    assert len(data) == 1, "The timeseries data could not be properly retrieved"


# import json
# with open('resources/stations.json', 'w') as f:
#     json.dump(stations, f)
