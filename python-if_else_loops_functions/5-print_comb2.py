#!/usr/bin/python3

for i in range(0, 100):
    if i == 99:
        print("{}".format(i), end="" + "\n")
        break
    print("{:02d}".format(i), end=", ")
