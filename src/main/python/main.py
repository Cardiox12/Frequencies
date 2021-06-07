from fbs_runtime.application_context.PySide2 import ApplicationContext
from package.window import Window

import sys

if __name__ == '__main__':
    app_ctx = ApplicationContext()
    window = Window(app_ctx)

    window.show()
    exit_code = app_ctx.app.exec_()
    sys.exit(exit_code)