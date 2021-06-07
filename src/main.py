from PySide2.QtWidgets import QApplication
from package.window import Window

import sys
import os

dirname, _ = os.path.split(os.path.abspath(__file__))
print(f"Running from {dirname}")

if __name__ == '__main__':
    app = QApplication()
    window = Window()

    window.show()
    sys.exit(app.exec_())
