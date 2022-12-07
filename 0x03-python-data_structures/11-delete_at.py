#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if my_list or idx < 0:
        if len(my_list) > 0 and idx < len(my_list):
            new_list = []
            for i in range(len(my_list)):
                if i == idx:
                    pass
                else:
                    new_list.append(my_list[i])
            return (new_list)
    return (my_list)
