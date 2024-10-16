#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

FILENAME = "add_item.json"


def main():
    """Main function to load, add, and save items to a JSON file."""
    try:
        items = load_from_json_file(FILENAME)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, FILENAME)


if __name__ == "__main__":
    main()
