#!/usr/bin/python3
"""Creating a base class"""

from os import path
import json


class Base:
    """
    ...
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        ...
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = []

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())

        filename = cls.__name__ + '.csv'
        with open(filename, 'w', encoding='utf-8') as file:
            csv_writer = csv.DictWriter(file, keys)
            csv_writer.writeheader()
            for dict in list_dicts:
                csv_writer.writerow(dict)

    @classmethod
    def load_from_file_csv(cls):
        import os.path

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        filename = cls.__name__ + '.csv'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                instance_list = []
                for row in csv_reader:
                    for key in keys:
                        row[key] = int(row[key])
                    instance_list.append(cls.create(**row))
                return instance_list
        else:
            return []
