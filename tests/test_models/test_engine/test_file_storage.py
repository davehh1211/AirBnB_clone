#!/usr/bin/python3


import console
import unittest
import json
import pep8
import models
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage
storefile = file_storage.FileStorage
classes = {"BaseModel": BaseModel}


class TestFileStorage(unittest.TestCase):
    def test_all_dict_returned(self):
        file = storefile()
        dicto = file.all()
        self.assertIs(dicto, file._FileStorage__objects)
        self.assertEqual(type(dicto), dict)

    def test_new(self):
        file = storefile()
        save = storefile._FileStorage__objects
        storefile._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                file.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, file._FileStorage__objects)
        storefile._FileStorage__objects = save

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        file = storefile()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = storefile._FileStorage__objects
        storefile._FileStorage__objects = new_dict
        file.save()
        storefile._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    # def test_save(self):

# class FileStorage:
#     """this class will store user info into a json file"""
#     __file_path = "file.json"
#     __objects = {}

#     def all(self):
#         """returns a dictionary"""
#         return FileStorage.__objects

#     def new(self, obj):
#         """sets a new id to a key"""
#         key = "{}.{}".format(obj.__class__.__name__, obj.id)
#         FileStorage.__objects[key] = obj

#     def save(self):
#         """serializes the dictionary to a json file"""
#         dict_jsonfile = {}
#         for key, value in FileStorage.__objects.items():
#             dict_jsonfile[key] = value.to_dict()
#         with open(FileStorage.__file_path, mode="w",
#                   encoding="UTF8") as jsonfile:
#             json.dump(dict_jsonfile, jsonfile)

#     def reload(self):
#         """deserializes the JSON file to a dictionary"""
#         try:
#             with open(FileStorage.__file_path, mode="r",
#                       encoding="UTF8") as jsonfile:
#                 dict_jsonfile = json.load(jsonfile)
#             for key, value in dict_jsonfile.items():
#                 obj = key.split(".")
#                 FileStorage.__objects[key] = eval(obj[0])(**value)
#         except Exception:
#             pass
