"""
    File:    file.py
    Purpose: Generic file object.
    Creator: WakandaO2 (16/03/2020)
"""

import os.path


class GenericFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.data = ""

    def is_archive(self):
        return isinstance(self.data, list)

    @staticmethod
    def replace_ext(filename, new_ext):
        return os.path.splitext(filename)[0] + f".{new_ext}"