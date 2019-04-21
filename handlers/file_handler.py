"""
    File:    file_handler.py
    Purpose: Generic file handler.
    Creator: WakandaO2 (21/04/2019)
"""


import os
import struct


class GenericFile(object):

    def __init__(self, filepath):
        self.path = filepath


class GenericFileHandler(object):
    """
    Generic file handler.
    """
    PARSE_FILE_MODE = "rb"
    CREATE_FILE_MODE = "wb"

    INTEGER_STRUCT = "I"

    @classmethod
    def _add_extension(cls, file_name):
        return \
            "{}.{}".format(os.path.splitext(file_name)[0], cls.EXTENSION)

    @classmethod
    def _read_integer(cls, opened_file):
        raw_data = opened_file.read(struct.calcsize(cls.INTEGER_STRUCT))
        return struct.unpack(cls.INTEGER_STRUCT, raw_data)[0]

    @classmethod
    def parse_file(cls, filepath):
        raise NotImplementedError()

    @classmethod
    def create_file(cls, file):
        raise NotImplementedError()
