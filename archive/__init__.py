import archive.pkg
import archive.zip


SUPPORTED_TYPES = {
    archive.pkg.EXTENSION: archive.pkg,
    archive.zip.EXTENSION: archive.zip
}

ARCHIVE_TYPES = {
    archive.pkg.EXTENSION: archive.pkg.PKGFile,
    archive.zip.EXTENSION: archive.zip.ZIPFile
}
