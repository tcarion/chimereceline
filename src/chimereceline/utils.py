import json

import requests
from requests.exceptions import HTTPError

from chimereceline.constants import API_SOS_URL, STATIONS_FILE


def try_request(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            response.raise_for_status()
        except HTTPError:
            raise
        except Exception:
            raise
        else:
            return response

    return wrapper


@try_request
def _req_get(url: str):
    stations_response = requests.get(url)
    return stations_response


def retrieve_stations() -> dict:
    return _req_get(API_SOS_URL + "/stations").json()


def read_stations():
    with open(STATIONS_FILE) as f:
        return json.load(f)
