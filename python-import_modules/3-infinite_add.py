#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    count = len(argv)
    total = 0

    for i in range(1, count):
        total += int(argv[i])

    print("{:d}".format(total))
