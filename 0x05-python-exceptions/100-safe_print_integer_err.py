#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except TypeError as excpt:
        sys.stderr.write(f"Exception: {excpt}\n")
        return (False)
    except ValueError as ept:
        sys.stderr.write(f"Exception: {ept}\n")
        return (False)
    else:
        return (True)
