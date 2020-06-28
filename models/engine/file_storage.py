#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """[summary]
                """
 
    def all(self):
        return FileStorage.__objects
        
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        dict_jsonfile = {}
        for key, value in FileStorage.__objects.items():
            dict_jsonfile[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="UTF8") as jsonfile:
            json.dump(dict_jsonfile, jsonfile)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r", encoding="UTF8") as jsonfile:
                dict_jsonfile = json.load(jsonfile)
            for key, value in dict_jsonfile.items():
                obj = key.split(".")
                FileStorage.__objects[key] = eval(obj[0])(**value)
        except Exception:
            pass
