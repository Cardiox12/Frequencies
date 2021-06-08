import os

API_DIR = os.path.dirname(os.path.abspath(__file__))

FREQUENCIES_FILE = os.path.join(API_DIR, "data", "airport-frequencies.csv")
TABLE_ROW_COUNT = 3
TABLE_LABELS = [
    "Description",
    "Type",
    "Frequency"
]

CSS_FILE = os.path.join("src", "package", "resources", "style", "style.css")
