"""
    File:    pkg_handler.py
    Purpose: PKG file handler.
    Creator: WakandaO2 (21/04/2019)

    The PKG file as described:

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


from handlers.file_handler import GenericFileHandler, GenericFile


class PKGFile(GenericFile):
    """
    Represents a PKG file. Created by parsing a PKG file.
    """
    pass


class PKGHandler(GenericFileHandler):
    """
    Wallpaper Engine's .pkg files handler.
    """
    INTEGER_STRUCT = "<I"
    EXTENSION = "pkg"

    PKG_VER_SIGNATURES = {
        1: b"PKGV0001",
        2: b"PKGV0002"
    }

    @classmethod
    def parse_file(cls, filepath):
        parsed_pkg = PKGFile(filepath)

        with open(filepath, cls.PARSE_FILE_MODE) as pkg_file:
            signature_length = cls._read_integer(pkg_file)

            parsed_pkg.signature = pkg_file.read(signature_length)
            files_count = cls._read_integer(pkg_file)

            parsed_pkg.files = []
            for f in range(files_count):
                current_filepath_len = cls._read_integer(pkg_file)

                current_filepath = str(pkg_file.read(current_filepath_len), 
                                       encoding="utf-8")
                current_file = GenericFile(current_filepath)

                current_file.offset = cls._read_integer(pkg_file)
                current_file.size = cls._read_integer(pkg_file)

                parsed_pkg.files.append(current_file)

            files_data_start = pkg_file.tell()

            for current_file in parsed_pkg.files:
                current_file_start = files_data_start + current_file.offset

                pkg_file.seek(current_file_start)
                current_file.data = pkg_file.read(current_file.size)

        return parsed_pkg

    @classmethod
    def create_file(cls, file_to_write, pkg_version=1):
        pkg_filepath = cls._add_extension(file_to_write.path)

        with open(pkg_filepath, cls.CREATE_FILE_MODE) as opened_pkg:
            cls._write_integer(opened_pkg,
                               len(cls.PKG_VER_SIGNATURES[pkg_version]))
            opened_pkg.write(cls.PKG_VER_SIGNATURES[pkg_version])

            cls._write_integer(opened_pkg, len(file_to_write.files))

            current_offset = 0

            for f in file_to_write.files:
                # We write a chunk of bytes and not a string.
                encoded_path = bytes(f.path, "utf-8")

                cls._write_integer(opened_pkg, len(encoded_path))
                opened_pkg.write(encoded_path)

                cls._write_integer(opened_pkg, current_offset)
                cls._write_integer(opened_pkg, len(f.data))

                current_offset += len(f.data)

            for f in file_to_write.files:
                opened_pkg.write(f.data)
