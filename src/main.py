from PySide2.QtWidgets import QApplication
from package.window import Window

import sys
import os

dirname = os.path.dirname(os.path.abspath(__file__))
CSS_FILE = os.path.join(dirname, "package", "resources", "style", "style.css")

if __name__ == '__main__':
    app = QApplication()
    window = Window(CSS_FILE)

    window.show()
    sys.exit(app.exec_())
