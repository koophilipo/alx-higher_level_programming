#!/usr/bin/python3

def element_at(key, val):
    y = len(key)
    if val >= y or val < 0:
        return (None)
    else:
        for i, num in enumerate(key):
            if i == val:
                return (num)
