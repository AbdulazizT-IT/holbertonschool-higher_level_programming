#!/usr/bin/python3

def no_c(my_string):
    s1 = ""
    for i in my_string:
        if i != "C" and i != "c":
            s1 += i
    return s1
