#!/usr/bin/python3
"""
LockedClass Module

This module defines the LockedClass, which restricts the creation of
instance attributes to only one specific attribute named 'first_name'.
This is achieved by using the __slots__ mechanism, which prevents
dynamic addition of attributes to instances of the class, thus
conserving memory and improving performance.
"""


class LockedClass:
    """
    LockedClass

    A class that prevents the dynamic creation of instance attributes
    other than 'first_name'. This is useful for enforcing a strict
    attribute structure within instances.

    Attributes:
        first_name (str): The only allowed attribute that can be set
                          dynamically.
    """

    __slots__ = ["first_name"]
