#!/usr/bin/python3

"""

Manage id attribute in all your future classes


"""
import json
import csv


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
        dummy = cls(1, 1)
        dummy.x = 0
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Create list of classes from json file"""
        file_name = cls.__name__+".json"
        try:
            with open(file_name, "r") as f:
                dict_str = f.read()
                list_dict = cls.from_json_string(dict_str)
                list_obj = []
                for obj in list_dict:
                    list_obj.append(cls.create(**obj))

                return list_obj
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes to csv file"""
        f_name = cls.__name__+".csv"
        with open(f_name, "w") as f:
            w = csv.writer(f)
            for obj in list_objs:
                if type(obj).__name__ == "Rectangle":
                    lst = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif type(obj).__name__ == "Square":
                    lst = [obj.id, obj.size, obj.x, obj.y]
                else:
                    raise TypeError("Must be list of \
rectangle/square instances")
                w.writerow(lst)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        f_name = cls.__name__+".csv"

        with open(f_name, "r") as f:
            readed_lists = csv.reader(f)
            obj_list = []

            for lst in readed_lists:
                dict_junk = {}

                if cls.__name__ == "Rectangle":
                    dict_junk["id"] = lst[0]
                    dict_junk["width"] = lst[1]
                    dict_junk["height"] = lst[2]
                    dict_junk["x"] = lst[3]
                    dict_junk["y"] = lst[4]

                elif cls.__name__ == "Square":
                    dict_junk["id"] = lst[0]
                    dict_junk["size"] = lst[1]
                    dict_junk["x"] = lst[2]
                    dict_junk["y"] = lst[3]
                obj_list.append(cls.create(**dict_junk))

        return obj_list
