#!/usr/bin/python3

def islower(c):
    """
    Returns True if c is lowercase, False otherwise.
    """
    # Check if the ASCII value of the character is within the lowercase range
    return ord('a') <= ord(c) <= ord('z')
