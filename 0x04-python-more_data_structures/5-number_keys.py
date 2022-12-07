#!/usr/bin/python3


def number_keys(a_dictionary):
    total = 0
    if a_dictionary:
        if len(a_dictionary) > 0:
            for i in a_dictionary:
                total += 1
    return (total)
