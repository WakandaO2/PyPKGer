"""
    File:    pkg_handler.py
    Purpose: ZIP archive file handler.
    Creator: WakandaO2 (21/04/2019)
"""

import zipfile

from handlers.file_handler import GenericFileHandler, GenericFile


class ZIPHandler(GenericFileHandler):
    """
    Represents ZIP archive file handler.
    """
    EXTENSION = "zip"
    ZIP_WRITE_MODE = "w"
    ZIP_READ_MODE = "a"

    @classmethod
    def parse_file(cls, filepath):
        parsed_zip = GenericFile(filepath)
        parsed_zip.files = []

        with zipfile.ZipFile(filepath, cls.ZIP_READ_MODE) as opened_zip:
            for filename in opened_zip.namelist():
                current_file = GenericFile(filename)
                current_file.data = opened_zip.read(filename)

                parsed_zip.files.append(current_file)

        return parsed_zip

    @classmethod
    def create_file(cls, file_to_write):
        zip_file_path = cls._add_extension(file_to_write.path)

        with zipfile.ZipFile(zip_file_path, cls.ZIP_WRITE_MODE) as opened_zip:
            for f in file_to_write.files:
                opened_zip.writestr(f.path, f.data)
