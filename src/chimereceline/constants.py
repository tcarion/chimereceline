from importlib.resources import files

API_SOS_URL = "https://geo.irceline.be/sos/api/v1/"

STATIONS_FILE = files("chimereceline.resources").joinpath("stations.json")
PHENOMENA_FILE = files("chimereceline.resources").joinpath("phenomena.json")
