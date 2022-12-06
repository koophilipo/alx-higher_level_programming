#!/usr/bin/python3

def element_at(key, val):
    y = len(key)
    if val >= y or val < 0:
        return (None)
    elif val < y:
        for i, num in enumerate(key):
            if i == val + 1:
                return (key.index(num))
