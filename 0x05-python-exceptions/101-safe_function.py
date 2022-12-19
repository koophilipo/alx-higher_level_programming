#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    val = 0
    try:
        val = fct(args[0], args[1])
    except ZeroDivisionError as excep:
        sys.stderr.write(f"Exception: {excep}\n")
        return (None)
    except IndexError as iderr:
        sys.stderr.write(f"Exception: {iderr}\n")
        return (None)
    except TypeError as tperr:
        sys.stderr.write(f"Exception: {tperr}\n")
        return (None)
    except ValueError as verr:
        sys.stderr.write(f"Exception: {verr}\n")
        return (None)
    else:
        return (val)
