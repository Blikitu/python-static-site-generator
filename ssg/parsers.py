from typing import List
from pathlib import Path
import shutil


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):

        if extension in self.extensions:
            return true
        else:
            return false

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError("This needs to be implemented")

    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            return file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(source, dest / path.relative_to(source))

    class ResourceParser(Parser):
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]

        def parse(self, path: Path, source: Path, dest: Path):
            copy(path, source, dest)
