#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            try:
                val1 = my_list_1[i]
                val2 = my_list_2[i]
                if not (isinstance(val1, (int, float)) and isinstance(val2, (int, float))):
                    print("wrong type")
                    result.append(0)
                else:
                    try:
                        div = val1 / val2
                    except ZeroDivisionError:
                        print("division by 0")
                        div = 0
                    result.append(div)
            except IndexError:
                print("out of range")
                result.append(0)
        finally:
            continue
    return result
