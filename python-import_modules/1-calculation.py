#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)
    print("{}{}{}{}{}".format(a, " + ", b, " = ", result_add))
    print("{}{}{}{}{}".format(a, " - ", b, " = ", result_sub))
    print("{}{}{}{}{}".format(a, " * ", b, " = ", result_mul))
    print("{}{}{}{}{}".format(a, " / ", b, " = ", result_div))
