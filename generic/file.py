"""
    File:    file.py
    Purpose: Generic files objects and utilities.
    Creator: WakandaO2 (16/03/2020)
"""

import os.path


class GenericFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.data = b""


class GenericArchive(GenericFile):
    def __init__(self, filename):
        super(GenericArchive, self).__init__(filename)
        self.data = []


def update_extension(filename, new_ext):
    """
    Update/Add the extension of a filename.
    """
    return os.path.splitext(filename)[0] + f".{new_ext}"