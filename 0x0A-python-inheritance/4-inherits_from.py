Task 4: Only Subclass of
#!/usr/bin/python3
"""
Define a function to check if an object is an instance of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to compare with.

    Returns:
    bool: True if obj is an instance of a_class subclass, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

