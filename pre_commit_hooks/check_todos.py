import argparse
import os


def main(argv=None):
    parser = argparse.ArgumentParser()
    args = parser.parse_args(argv)

    for filename in args.filenames:
        _, extension = os.path.splitext(filename.lower())
        print(f"{filename}, {extension}")
