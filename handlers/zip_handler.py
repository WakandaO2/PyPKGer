"""
    File:    pkg_handler.py
    Purpose: ZIP archive file handler.
    Creator: WakandaO2 (21/04/2019)
"""


from zipfile import ZipFile

from handlers.file_handler import GenericFileHandler


class ZIPHandler(GenericFileHandler):
    """
    Represents ZIP archive file handler.
    """
    EXTENSION = "zip"
    ZIP_WRITE_MODE = "w"

    @classmethod
    def parse_file(cls, filepath):
        raise NotImplementedError()

    @classmethod
    def create_file(cls, file_to_write):
        zip_file_path = cls._add_extension(file_to_write.path)

        with ZipFile(zip_file_path, cls.ZIP_WRITE_MODE) as opened_zip:
            for f in file_to_write.files:
                opened_zip.writestr(f.path, f.data)
