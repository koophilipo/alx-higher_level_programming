#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    new_set = set()
    if set_1 and set_2:
        if len(set_1) > 0 or len(set_2) > 0:
            diff_set = (set_1 - set_2) | (set_2 - set_1)
            return (diff_set)
    return (new_set)
