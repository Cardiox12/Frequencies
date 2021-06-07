import pandas

from package.api.constants import FREQUENCIES_FILE


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
        self.data = None

    def get_frequency_by_oaci(self, oaci: str, filter = None):
        self.data = self.frequencies[self.frequencies["oaci"] == oaci.upper()].to_dict()
        if filter:
            return self.get_by_labels_(filter)
        return self.data

    def get_by_labels_(self, labels):
        new_dict = {}

        if self.data:
            for label in labels:
                new_dict[label] = self.data.get(label)

        return new_dict

