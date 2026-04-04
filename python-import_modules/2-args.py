#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("{} argument{}{}".format(
        argc,
        "" if argc == 1 else "s",
        ":" if argc > 0 else "."
    ))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
