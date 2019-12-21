"""
    File:    pypkger.py
    Purpose: PyPKGer - Extract and create .pkg
                       files accepted by Wallpaper Engine.
    Creator: WakandaO2 (21/04/2019)
"""

import argparse
import os
import sys

from handlers import HANDLERS_BY_EXTENSION


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Convert to/from Wallpaper Engine's PKG format.")
    parser.add_argument("-ot", "--output-type", help="file type to convert to", required=True)
    parser.add_argument("file_paths", help="paths of files to convert", nargs="+")

    parsed_args = parser.parse_args()
    parsed_args.output_type = str.lower(parsed_args.output_type)
    return parsed_args


def main(argv):
    parsed_args = parse_args(argv)

    for file_path in parsed_args.file_paths:
        file_ext = str.lower(os.path.splitext(file_path)[1][1:])

        if file_ext == parsed_args.output_type:
            print("Skipping file \"{}\"".format(file_path))
            continue

        try:
            parsed_file = \
                HANDLERS_BY_EXTENSION[file_ext].parse_file(file_path)

            print("Converting file \"{}\" to {}.".format(file_path, parsed_args.output_type))
            HANDLERS_BY_EXTENSION[parsed_args.output_type].create_file(parsed_file)

        except KeyError:
            print("\"{}\" file is not supported.".format(file_ext))
        except NotImplementedError:
            print("\"{}\" file is not yet supported.".format(file_ext))


if __name__ == "__main__":
    main(sys.argv)
