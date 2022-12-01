#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        x = number * (-1)
        x %= 10
        x *= -1
    else:
        x = number % 10
    return (x)
