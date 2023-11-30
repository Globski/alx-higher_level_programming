#!/usr/bin/python3

for digits in range(10):
    for digit1 in range(digits + 1, 10):
        if digits < 9:
            print("{:d}{:d}, ".format(digits, digit1), end="")
        else:
            print("{:d}{:d}".format(digits, digit1))
