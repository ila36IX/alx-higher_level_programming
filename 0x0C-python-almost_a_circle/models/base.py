#!/usr/bin/python3

"""

Manage id attribute in all your future classes


"""
import json


class Base():
    """
    The Base class
    args:
        id: Integer
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            self.id = Base.inc_id()

    @classmethod
    def inc_id(cls):
        """Increament nb_object"""
        cls.__nb_objects += 1
        return cls.__nb_objects

    @classmethod
    def reset(cls):
        """Reset the nb_object varaible"""
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert class object to string"""

        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"

        dic_list = []
        for obj in list_dictionaries:
            if type(obj).__name__ == "Rectangle":
                dic_list.append(obj.to_dictionary())
            elif type(obj).__name__ == "Square":
                dic_list.append(obj.to_dictionary())
            elif isinstance(obj, dict):
                dic_list.append(obj)
            else:
                raise TypeError("Must be a list of dicts")

        return json.dumps(dic_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """write to json file"""
        file_name = cls.__name__+".json"
        if list_objs is None:
            with open(file_name, "w") as f:
                f.write("[]")
            pass

        with open(file_name, "w") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Deserialize"""
        if json_string is None:
            return []
        args_list = json.loads(json_string)
        return args_list

    @classmethod
    def create(cls, **dictionary):
        """Create new instance"""
        dummy = cls(69, 5, 3, 6, 9)
        dummy.update(**dictionary)
        return dummy
