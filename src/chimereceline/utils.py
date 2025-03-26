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
def _req_get(*args, **kwargs):
    stations_response = requests.get(*args, **kwargs)
    return stations_response


def _read_json(file):
    rawdata = file.read_text(encoding="utf-8")
    return json.loads(rawdata)


def retrieve_stations() -> dict:
    return _req_get(API_SOS_URL + "/stations").json()


def retrieve_phenomena() -> dict:
    return _req_get(API_SOS_URL + "/phenomena").json()


def retrieve_timeseries(id_sta, id_phen) -> dict:
    req_url = API_SOS_URL + "/timeseries"
    payload = {"station": id_sta, "phenomenon": id_phen}
    return _req_get(req_url, params=payload).json()


def retrieve_timeserie_data(id_ts: int, timespan: str = "") -> dict:
    req_url = API_SOS_URL + "/timeseries" + f"/{id_ts}" + "/getData"
    payload = {"timespan": timespan} if timespan else {}
    return _req_get(req_url, params=payload).json()


def read_stations():
    return _read_json(STATIONS_FILE)


def read_phenomena():
    return _read_json(PHENOMENA_FILE)
