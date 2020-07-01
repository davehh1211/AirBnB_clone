#!/usr/bin/python3
"""file storage module"""
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
    """test for class file storage"""

    def test_all_dict_returned(self):
        """test the method all when returns dict"""
        file = storefile()
        dicto = file.all()
        self.assertIs(dicto, file._FileStorage__objects)
        self.assertEqual(type(dicto), dict)

    def test_new(self):
        """test the method new at the creation of new object"""
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

    def test_base_pep8_conformance_file_storage(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['/models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 1)

    def test_base_pep8_conformance_filesto_test(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            '/tests/test_models/test_engine/test_file_storageconsole.py'])
        self.assertEqual(result.total_errors, 1)

    def test_file_storage_docstring(self):
        """test docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "console.py needs a docstring")
