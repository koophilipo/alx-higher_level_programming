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
    except UnboundLocalError as unerr:
        sys.stderr.write(f"Exception: {unerr}\n")
        return (None)
    except NameError as nerr:
        sys.stderr.write(f"Exception: {nerr}\n")
        return (None)
    except FloatingPointError as ferr:
        sys.stderr.write(f"Exception: {ferr}\n")
        return (None)
    except OverflowError as overr:
        sys.stderr.write(f"Exception: {overr}\n")
        return (None)
    else:
        return (val)
