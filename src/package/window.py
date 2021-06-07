from PySide2 import QtWidgets

from package.api.constants import TABLE_ROW_COUNT, TABLE_LABELS, CSS_FILE
from package.api.frequencies import Frequencies


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.frequencies = Frequencies()
        self.setWindowTitle("Frequencies")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.set_objects_name()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.airport_line_edit = QtWidgets.QLineEdit()
        self.find_button = QtWidgets.QPushButton("Find")
        self.freqs_table = QtWidgets.QTableWidget()

    def set_objects_name(self):
        self.airport_line_edit.setObjectName("airportLineEdit")
        self.find_button.setObjectName("findButton")
        self.freqs_table.setObjectName("freqsTable")

    def modify_widgets(self):
        # Size
        self.setFixedSize(600, 900)
        self.airport_line_edit.setFixedSize(330, 50)
        self.find_button.setFixedSize(160, 50)
        self.freqs_table.setFixedSize(536, 750)

        # Placeholder
        self.airport_line_edit.setPlaceholderText("OACI Code")
        self.freqs_table.setColumnCount(TABLE_ROW_COUNT)
        self.freqs_table.setHorizontalHeaderLabels(TABLE_LABELS)

        # Style
        self.freqs_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.freqs_table.verticalHeader().setVisible(False)

        with open(CSS_FILE, "r") as f:
            self.setStyleSheet(f.read())

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.airport_line_edit, 0, 0, 1, 1)
        self.main_layout.addWidget(self.find_button, 0, 1, 1, 1)
        self.main_layout.addWidget(self.freqs_table, 1, 0, 1, 2)

    def setup_connections(self):
        self.find_button.clicked.connect(self.on_find_button_clicked)
        self.airport_line_edit.returnPressed.connect(self.on_find_button_clicked)

    def on_find_button_clicked(self):
        oaci = self.airport_line_edit.text()

        if oaci:
            data = self.frequencies.get_frequency_by_oaci(oaci, [
                Frequencies.COL_DESCRIPTION,
                Frequencies.COL_FREQUENCY,
                Frequencies.COL_TYPE
            ])
            if data:
                rows_count = len(data[Frequencies.COL_DESCRIPTION])
                self.fill_table_widget(rows_count, data)

    def fill_table_widget(self, row_count, data):
        self.freqs_table.setRowCount(row_count)

        for index, key in enumerate(data.get(Frequencies.COL_DESCRIPTION)):
            desc = data.get(Frequencies.COL_DESCRIPTION).get(key)
            type = data.get(Frequencies.COL_TYPE).get(key)
            freq = f"{data.get(Frequencies.COL_FREQUENCY).get(key)} mHz"


            self.freqs_table.setItem(index, 0, QtWidgets.QTableWidgetItem(desc))
            self.freqs_table.setItem(index, 1, QtWidgets.QTableWidgetItem(type))
            self.freqs_table.setItem(index, 2, QtWidgets.QTableWidgetItem(freq))




