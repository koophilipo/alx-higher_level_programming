#!/usr/bin/python3


def uniq_add(my_list=[]):
    total = 0
    if my_list:
        if len(my_list) > 0:
            new_list = my_list.copy()
            new_list.sort()
            for i in range(len(new_list)):
                if i == len(new_list) - 1:
                    total += new_list[i]
                elif new_list[i] != new_list[i + 1]:
                    total += new_list[i]
    return (total)
