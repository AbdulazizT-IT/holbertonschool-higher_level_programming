#!/usr/bin/python3

def pow(a, b):
    count = 0
    result = 1
    if b == 0:
        return 1
    elif b > 0:
        while count < b:
            result *= a
            count += 1
        return result
    else:
        b = -1 * b
        while count < b:
            result *= a
            count += 1
        result = 1 / result
        return result
