"""
    File:       raw.py
    Purpose:    Raw directory import/extract.
    Creator:    WakandaO2 (16/03/2020)
"""

import os
import os.path

from generic.file import GenericFile, GenericArchive, update_extension


EXTENSION = '' 


class RawDirectory(GenericArchive):
    """
    This is not an archive but actually a structure of directories
    containing the files.
    """
    def __init__(self, basedir):
        super(RawDirectory, self).__init__(os.path.realpath(basedir))
        self._read_dir(basedir)

    def _read_dir(self, basedir):
        for this_dir, _, dir_files in os.walk(basedir):
            for dir_file in dir_files:
                this_filepath = os.path.join(this_dir, dir_file)
                this_file = GenericFile(this_filepath.replace(basedir, "")[1:])
                
                with open(this_filepath, "rb") as opened_file:
                    this_file.data = opened_file.read()
                
                self.data.append(this_file)


def export_archive(archive):
    """
    Export the archive as RAW (i.e: extract it).
    """
    basedir = update_extension(archive.filename, EXTENSION)
    os.mkdir(basedir)

    for in_file in archive.data:
        in_file_path = os.path.join(basedir, in_file.filename)
        os.makedirs(os.path.dirname(in_file_path), exist_ok=True)

        with open(os.path.join(in_file_path), "wb") as opened_file:
            opened_file.write(in_file.data)
