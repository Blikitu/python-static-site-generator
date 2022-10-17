from os import mkdir
from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = Path.path(source)
        self.dest = Path.path(dest)

    def create_dir(self, path):
        directory = path.relative_to(self.source)
        mkdir(directory, True, True)

    def build(self):
        mkdir(self.dest, True, True)
        for x in self.source.rglob("*"):
            path = Path.path(x)
            if path.isdir():
                self.create_dir(path)
