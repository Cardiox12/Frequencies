from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow

import sys

if __name__ == '__main__':
    app_ctx = ApplicationContext()

    exit_code = app_ctx.app.exec_()
    sys.exit(exit_code)