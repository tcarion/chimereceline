from datetime import datetime
from typing import List, Optional

from chimereceline.collection import SosCollection
from chimereceline.phenomena import Phenomenon
from chimereceline.stations import Station
from chimereceline.utils import retrieve_timeserie_data, retrieve_timeseries


class TimeSerie:
    """Create a TimeSerie object from a Station and a Phenomenon.

    Upon creation, it retrieves the unique timeserie id corresponding to the combination of station and phenomenon.
    The specific data must then be retrieved with TODO
    """

    station: Station
    phenomenon: Phenomenon

    id: int
    label: str
    """units of measure"""
    uom: str
    _timespan: List[datetime] = []
    times: List[datetime] = []
    values: List[Optional[float]] = []

    def __init__(self, sta: Station, phen: Phenomenon):
        data = self._retrieve_ts(sta.id, phen.id)
        self.station = sta
        self.phenomenon = phen

        self.id = int(data["id"])
        self.label = data["label"]
        self.uom = data["uom"]

    @classmethod
    def init_by_id(cls, coll: SosCollection, sta_id: int, phen_id: int):
        s = coll.get_by_id(sta_id, "Station")
        p = coll.get_by_id(phen_id, "Phenomenon")
        return cls(s, p)

    def _retrieve_ts(self, id_sta: int, id_phen: int):
        response = retrieve_timeseries(id_sta, id_phen)
        ts = response.json()
        if len(ts) == 0:
            raise RuntimeError(
                f"The timeserie response is empty for request: {response.url}"
            )
        if len(ts) > 1:
            raise RuntimeError(
                f"{len(ts)} timeserie products were retrieved for station.id={id_sta} and phen.id={id_phen}. Only 1 timeserie data can be downloaded at once."
            )
        return ts[0]

    def has_data(self):
        return True if self.data else False

    def get_data(
        self, starttime: Optional[datetime] = None, endtime: Optional[datetime] = None
    ):
        if not starttime and not endtime:
            r = retrieve_timeserie_data(self.id).json()
        else:
            if not starttime:
                raise RuntimeError(
                    "Retrieval needs at least a start time, or neither of both"
                )
            strstart = starttime.isoformat()

            # if no end datetime is provided, we consider the actual time
            strend = endtime.isoformat() if endtime else datetime.now().isoformat()
            timespan = strstart + "/" + strend
            r = retrieve_timeserie_data(self.id, timespan).json()

        data = r["values"]

        # d['timestamp'] is in number of millisecond from 1970-01-01
        times = [datetime.fromtimestamp(d["timestamp"] / 1000) for d in data]
        values = [d["value"] for d in data]

        self.times = times
        self.values = values
        return times, values

    @property
    def timespan(self):
        """Retrieved start and end date of the time serie"""
        return [self.times[0], self.times[-1]] if self.times else []

    def __repr__(self):
        return f"TimeSerie object with label: {self.label} and units: {self.uom}"
