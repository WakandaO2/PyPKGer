"""
    File:    py_we_pkg.py
    Purpose: PyWallpaperEnginePKG -
             Extract and create .pkg files accepted by Wallpaper Engine.
    Creator: WakandaO2 (21/04/2019)
"""

import sys

from handlers.pkg_handler import PKGHandler
# from handlers.zip_handler import ZIPHandler


def parse_args(args):
    return args[1:]


def main(argv):
    args = parse_args(argv)

    for pkg_filepath in args:
        parsed_pkg_file = PKGHandler.parse_file(pkg_filepath)
        # TODO: Add ZIP file creation after ZIPHandler implementation.


if __name__ == "__main__":
    main(sys.argv)