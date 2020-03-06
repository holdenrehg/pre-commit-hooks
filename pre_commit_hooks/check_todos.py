import argparse
import os
import re
from collections import deque, OrderedDict


def get_comments(identifier, lines, extension):
    comment_lines = []
    for index, line in enumerate(lines):
        if identifier in line and not f"ignore:{identifier}".lower() in line:
            line = line.strip("\n").strip()
            comment_lines.append(f"(l{index + 1}): {line}")
    return comment_lines

def get_todo_comments(lines, extension):
    return get_comments("TODO", lines, extension)  # ignore:todo

def get_fixme_comments(lines, extension):
    return get_comments("FIXME", lines, extension)  # ignore:fixme

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    rv = 0
    todos = []
    fixmes = []

    for filename in args.filenames:
        _, extension = os.path.splitext(filename.lower())
        with open(filename, "r") as file_:
            lines = file_.readlines()
            todos += list(map(lambda line: f"[WARN] {filename} " + line,get_todo_comments(lines, extension)))
            fixmes += list(map(lambda line: f"[ERROR] {filename} "+ line, get_fixme_comments(lines, extension)))

    if todos:
        print("\n".join(todos))
    if fixmes:
        rv = 1
        print("\n".join(fixmes))

    return rv

if __name__ == "__main__":
    exit(main())
