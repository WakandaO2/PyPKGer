"""
    File:    pypkger.py
    Purpose: PyPKGer - Extract and create .pkg
                       files accepted by Wallpaper Engine.
    Creator: WakandaO2 (21/04/2019)
"""

import os
import sys

from handlers import HANDLERS_BY_EXTENSION
from handlers.pkg_handler import PKGHandler, PKGFile
from handlers.zip_handler import ZIPHandler


def main(args):
    for filepath in args:
        filepath_ext = os.path.splitext(filepath)[1][1:]

        try:
            parsed_file = \
                HANDLERS_BY_EXTENSION[filepath_ext].parse_file(filepath)

            print type(parsed_file)
            if isinstance(parsed_file, PKGFile):
                ZIPHandler.create_file(parsed_file)
            else:
                PKGHandler.create_file(parsed_file)

        except KeyError:
            print "\"{}\" file is not supported.".format(filepath_ext)
        except NotImplementedError:
            print "\"{}\" file is not yet supported.".format(filepath_ext)


if __name__ == "__main__":
    main(sys.argv[1:])
