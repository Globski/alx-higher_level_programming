#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
msg = "Last digit of {} is {} and is".format(number, last_digit)

if number < 0:
    last_digit = -last_digit
    msg = "Last digit of {} is {} and is".format(number, last_digit)

if last_digit > 5:
    print("{} greater than 5".format(msg))
elif last_digit == 0:
    print("{} 0".format(msg))
else:
    print("{} less than 6 and not 0".format(msg))
