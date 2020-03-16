from generic.file import GenericArchive

import archive.raw
import archive.pkg
import archive.zip


SUPPORTED_EXPORT_TYPES = {
    archive.raw.EXTENSION: archive.raw,
    archive.pkg.EXTENSION: archive.pkg,
    archive.zip.EXTENSION: archive.zip
}

ARCHIVE_TYPES = {
    archive.raw.EXTENSION: archive.raw.RawDirectory,
    archive.pkg.EXTENSION: archive.pkg.PKGArchive,
    archive.zip.EXTENSION: archive.zip.ZIPArchive
}

ARCHIVE_EXTRACT_FMT = 'Extracting archive "{}".'
ARCHIVE_EXPORT_FMT = 'Exporting archive "{}" as "{}".'


def export(export_archive, export_type):
    """
    Export an archive to a file in the given type.
    """
    if not isinstance(export_archive, GenericArchive):
        raise TypeError("The exported file is not an archive!")

    if export_type == archive.raw.EXTENSION:
        print(f'Extracting "{export_archive.filename}"')
    else:
        print(f'Exporting "{export_archive.filename}" as "{export_type}"')
    
    SUPPORTED_EXPORT_TYPES[export_type].export_archive(export_archive)