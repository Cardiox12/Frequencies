import os


class ContextManager:
    def __init__(self, basedir):
        self.basedir = os.path.dirname(os.path.abspath(basedir))
        self.resources_dirname = "resources"
        self.style_dirname = "style"
        self.data_dirname = "data"


    def get_style(self, filename):
        return os.path.join(self.basedir, self.resources_dirname, self.style_dirname, filename)

    def get_data(self, filename):
        return os.path.join(self.basedir, self.resources_dirname, self.data_dirname, filename)
