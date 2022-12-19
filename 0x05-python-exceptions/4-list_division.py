#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        x = 0
        try:
            x = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            new_list.append(x)
        except ZeroDivisionError:
            print("division by zero")
            new_list.append(x)
        except IndexError:
            print("out of range")
            new_list.append(x)
        else:
            new_list.append(x)
    return (new_list)
