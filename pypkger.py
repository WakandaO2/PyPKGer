#!/usr/bin/env python3
"""
    File:    pypkger.py
    Purpose: PyPKGer - Extract and create .pkg
                       files accepted by Wallpaper Engine.
    Creator: WakandaO2 (21/04/2019)
"""

import argparse
import os
import sys

import archive


def parse_args():
    parser = argparse.ArgumentParser(description="Convert to/from Wallpaper Engine's PKG format.")
    parser.add_argument("-ot", "--output-type", help="Output file type", 
                        default="", type=str.lower)
    parser.add_argument("file_paths", help="paths of files to convert", nargs="+")

    parsed_args = parser.parse_args()
    return parsed_args


def main(argv):
    for file_path in argv.file_paths:
        file_ext = str.lower(os.path.splitext(file_path)[1][1:])

        if file_ext == argv.output_type:
            print(f'Skipping file "{file_path}"')
            continue

        try:
            parsed_archive = archive.ARCHIVE_TYPES[file_ext](file_path)
            archive.export(parsed_archive, argv.output_type)

        except KeyError:
            print(f'"{file_ext}" file is not supported.')


if __name__ == "__main__":
    main(parse_args())
