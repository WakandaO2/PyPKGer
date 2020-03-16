from generic.file import GenericArchive

import archive.pkg
import archive.zip

SUPPORTED_TYPES = {
    archive.pkg.EXTENSION: archive.pkg,
    archive.zip.EXTENSION: archive.zip
}

ARCHIVE_TYPES = {
    archive.pkg.EXTENSION: archive.pkg.PKGArchive,
    archive.zip.EXTENSION: archive.zip.ZIPArchive
}


def export(archive, export_type):
    if not isinstance(archive, GenericArchive):
        raise TypeError("The exported file is not an archive!")

    SUPPORTED_TYPES[export_type].export_archive(archive)