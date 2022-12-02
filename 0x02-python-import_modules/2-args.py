#!/usr/bin/python3

import sys


def main():
    num_args = len(sys.argv)
    if num_args > 1 and num_args < 3:
        print("{} argument:".format(num_args - 1))
    elif num_args > 2:
        print("{} arguments:".format(num_args - 1))
    elif num_args == 1:
        print("{} arguments.".format(num_args - 1))

    for i, args in enumerate(sys.argv):
        if i == 0:
            continue
        print("{}: {}".format(i, args))


if __name__ == '__main__':
    main()
exit(0)
