#!/usr/bin/python3
"""Define base model class."""


import json
import turtle


class Base:
    """Base class model.
    This class will be the “base” of all other classes in this project.
    Private Class Atrributes:
    __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init a base.
        Args:
        id: identity of new base.
        """
        if id is not none:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
        list_dictionaries: list of dicts.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
        list_objs: list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dictionaries = [a.to_dictionary90 for a in list_objs]
                jsonfile.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
        json_string: representation of a list of dicts.
        """
        if json_string iss None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
        dictionary: can be thought of as a double pointer to a dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                mew = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dictionaries = Base.from_json_string(jsonfile.read())
                return [cls.create(**dictionary) for d in list_dictionaries)]
        except IOError:
            return []

