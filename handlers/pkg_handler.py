"""
    File:    file_handler.py
    Purpose: Generic file handler.
    Creator: WakandaO2 (21/04/2019)

    The PKG file as described:

    struct pkg_header {
        int signature_length;
        char signature[signature_length];
        int files_count;
        struct file_metadata {
            int file_name_length;
            char file_name[file_name_length];
            int offset_in_file; /* the offset is from AFTER the header
                                   (e.g. the first file is in offset 0). */
            int file_size;
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

    @classmethod
    def parse_file(cls, filepath):
        parsed_pkg = PKGFile(filepath)

        with open(filepath, cls.PARSE_FILE_MODE) as pkg_file:
            signature_length = cls._parse_integer(pkg_file)

            parsed_pkg.signature = pkg_file.read(signature_length)
            files_count = cls._parse_integer(pkg_file)

            parsed_pkg.files = []
            for f in range(files_count):
                current_filepath_len = cls._parse_integer(pkg_file)

                current_filepath = pkg_file.read(current_filepath_len)
                current_file = GenericFile(current_filepath)

                current_file.offset = cls._parse_integer(pkg_file)
                current_file.size = cls._parse_integer(pkg_file)

                parsed_pkg.files.append(current_file)

            files_data_start = pkg_file.tell()

            for current_file in parsed_pkg.files:
                current_file_start = files_data_start + current_file.offset

                pkg_file.seek(current_file_start)
                current_file.data = pkg_file.read(current_file.size)

        return parsed_pkg

    @classmethod
    def create_file(cls, file):
        raise NotImplementedError()
