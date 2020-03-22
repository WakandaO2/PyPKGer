"""
    File:    zip.py
    Purpose: ZIP archive import/export.
    Creator: WakandaO2 (21/04/2019)
"""

import zipfile

from generic.file import GenericFile, GenericArchive, update_extension

EXTENSION = "zip"


class ZIPArchive(GenericArchive):
    """
    Represents a ZIP archive.
    """
    def __init__(self, filename):
        super(ZIPArchive, self).__init__(filename)

        with zipfile.ZipFile(filename, "a") as opened_zip:
            for filename in opened_zip.namelist():
                current_file = GenericFile(filename)
                current_file.data = opened_zip.read(filename)

                self.data.append(current_file)


def export_archive(exported_file):
    """
    Export an archive in ZIP format.
    """
    exported_filename = update_extension(exported_file.filename, EXTENSION)

    with zipfile.ZipFile(exported_filename, "w") as opened_zip:
        for in_file in exported_file.data:
            opened_zip.writestr(in_file.filename, in_file.data)
