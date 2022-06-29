#!/usr/bin/python3
for num in range(1, 90):
    if num < 10:
        print("0{:d}".format(num), end=", ")
    elif num == 89:
        print(num)
    else:
        print("{:d}".format(num), end=", ")
