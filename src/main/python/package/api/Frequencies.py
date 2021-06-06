import pandas

from constants import FREQUENCIES_FILE


class Frequencies:
    COL_ID = "id"
    COL_AIRPORT_REF = "airport_ref"
    COL_OACI = "oaci"
    COL_TYPE = "type"
    COL_DESCRIPTION = "description"
    COL_FREQUENCY = "frequency_mhz"

    def __init__(self):
        self.filename = FREQUENCIES_FILE
        self.frequencies = pandas.read_csv(self.filename)

    def get_frequency_by_oaci(self, oaci: str):
        return self.frequencies[self.frequencies["oaci"] == oaci.upper()].to_dict()
