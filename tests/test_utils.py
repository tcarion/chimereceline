from importlib import reload

import pytest

## TODO: remove these lines
import chimereceline.utils

reload(chimereceline.utils)
reload(chimereceline.constants)
from chimereceline.constants import API_SOS_URL
from chimereceline.utils import _req_get, read_stations, retrieve_stations


def test_retrieve_stations():
    with pytest.raises(Exception):
        _req_get(API_SOS_URL + "/foo")

    web_stations = retrieve_stations()
    file_stations = read_stations()

    assert web_stations == file_stations, (
        "The saved stations are different than the API ones"
    )


# import json
# with open('resources/stations.json', 'w') as f:
#     json.dump(stations, f)
