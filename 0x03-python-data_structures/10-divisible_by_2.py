#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list:
        if len(my_list) > 0:
            new_list = []
            for i in range(len(my_list)):
                new_list.append(True if (my_list[i] % 2) == 0 else False)
            return (new_list)
    return (None)
