#!/usr/bin/python3


def common_elements(set_1, set_2):
    empt_set = {}
    if set_1 and set_2:
        if len(set_1) > 0 and len(set_2) > 0:
            new_set = set_1.intersection(set_2)
            return (new_set)
    return (empt_set)
