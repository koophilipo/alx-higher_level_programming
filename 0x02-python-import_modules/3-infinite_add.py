#!/usr/bin/python3

import sys


def main():
    sum_args = 0
    for x, args in enumerate(sys.argv):
        if x == 0:
            continue
        sum_args += int(args)
    print("{:d}".format(sum_args))


if __name__ == '__main__':
    main()
exit(0)
