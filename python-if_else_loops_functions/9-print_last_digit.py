#!/usr/bin/python3

def print_last_digit(number):
    if number == 0:
        print(0, end="")
        return 0
    elif number > 0:
        num = number % 10
        print(num, end="")
        return num
    else:
        num = (-number % 10)
        print(num, end="")
        return num
