import json

import requests
from requests.exceptions import HTTPError

from chimereceline.constants import API_SOS_URL, PHENOMENA_FILE, STATIONS_FILE


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


def _read_json(file):
    rawdata = file.read_text(encoding="utf-8")
    return json.loads(rawdata)


def retrieve_stations() -> dict:
    return _req_get(API_SOS_URL + "/stations").json()


def retrieve_phenomena() -> dict:
    return _req_get(API_SOS_URL + "/phenomena").json()


def read_stations():
    return _read_json(STATIONS_FILE)


def read_phenomena():
    return _read_json(PHENOMENA_FILE)
