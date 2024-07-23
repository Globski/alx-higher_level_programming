#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all integers divisible by 2 in a list."""
    return [num % 2 == 0 for num in my_list]
