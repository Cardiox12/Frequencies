from PySide2.QtWidgets import QApplication
from package.window import Window
from package.api.context_manager import ContextManager

import sys


if __name__ == '__main__':
    ctx = ContextManager(__file__)
    app = QApplication()
    window = Window(ctx)

    window.show()
    sys.exit(app.exec_())
