#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    new_list = my_list.copy()
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
