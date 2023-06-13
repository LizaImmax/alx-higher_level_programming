#!/usr/bin/python3
"""Module 9-add_item.
Adds all arguments to a Python list,
and then save them to a file.
"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (any): object to be serialized

    """
    import json

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
