"""
    File:    pkg.py
    Purpose: PKG archive import/export.
    Creator: WakandaO2 (21/04/2019)

    The PKG archive as described:

    struct pkg_header {
        unsigned int signature_length;
        char signature[signature_length];
        int files_count;
        struct file_metadata {
            unsigned int file_name_length;
            char file_name[file_name_length];
            unsigned int offset_in_file; /* the offset is from AFTER the header
                                            (e.g. the first file is in offset 0). */
            unsigned int file_size;
        } files_metadata[files_count];
    };

    after the header, the files are concatenated as-is without seperators.
"""

import struct

from generic.file import GenericFile, GenericArchive, update_extension


EXTENSION = "pkg"

PKG_INTEGER_FMT = "<I"
PKG_INTEGER_SIZE = struct.calcsize(PKG_INTEGER_FMT)

PKG_VERSION_SIGNATURES = {
    1: b"PKGV0001",
    2: b"PKGV0002"
}


class PKGArchive(GenericArchive):
    """
    Wallpaper Engine's .pkg archive.
    """
    def __init__(self, filename):
        super(PKGArchive, self).__init__(filename)
        self._parse_pkg(filename)

    def _parse_pkg(self, pkg_filepath):
        opened_pkg = open(pkg_filepath, "rb")

        signature_len = struct.unpack(PKG_INTEGER_FMT, opened_pkg.read(PKG_INTEGER_SIZE))[0]
        self.signature = opened_pkg.read(signature_len)

        files_count = struct.unpack(PKG_INTEGER_FMT, opened_pkg.read(PKG_INTEGER_SIZE))[0]
        files_info = []

        for _ in range(files_count):
            this_filename_len = struct.unpack(PKG_INTEGER_FMT, opened_pkg.read(PKG_INTEGER_SIZE))[0]
            this_filename = str(opened_pkg.read(this_filename_len), "utf-8")
            this_file = GenericFile(this_filename)

            this_file_offset = struct.unpack(PKG_INTEGER_FMT, opened_pkg.read(PKG_INTEGER_SIZE))[0]
            this_file_size = struct.unpack(PKG_INTEGER_FMT, opened_pkg.read(PKG_INTEGER_SIZE))[0]

            files_info.append((this_file, this_file_size, this_file_offset))

        data_start = opened_pkg.tell()

        for file_info in files_info:
            this_file_start = data_start + file_info[2]
            opened_pkg.seek(this_file_start)
            file_info[0].data = opened_pkg.read(file_info[1])
            self.data.append(file_info[0])

        opened_pkg.close()


def export_archive(exported_file, pkg_version=1):
    """
    Export an archive in PKG format.
    """
    export_filepath = update_extension(exported_file.filename, EXTENSION)
    
    exported_data = struct.pack(PKG_INTEGER_FMT, len(PKG_VERSION_SIGNATURES[pkg_version]))
    exported_data += PKG_VERSION_SIGNATURES[pkg_version]
    exported_data += struct.pack(PKG_INTEGER_FMT, len(exported_file.data))

    current_offset = 0

    for in_file in exported_file.data:
        encoded_filename = bytes(in_file.filename, "utf-8")

        exported_data += struct.pack(PKG_INTEGER_FMT, len(encoded_filename))
        exported_data += encoded_filename

        exported_data += struct.pack(PKG_INTEGER_FMT, current_offset)
        exported_data += struct.pack(PKG_INTEGER_FMT, len(in_file.data))

    for in_file in exported_file.data:
        exported_data += in_file.data

    with open(export_filepath, "wb") as opened_pkg:
        opened_pkg.write(exported_data)
