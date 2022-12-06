#!/usr/bin/python3

def element_at(key, val):
    y = len(key)
    print("{}".format(y))
    if val >= y or val < 0:
        return (None)
    elif val < y:
        return (key.index(val))
