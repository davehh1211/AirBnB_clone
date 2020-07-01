#!/usr/bin/python3
"""City test module"""
import unittest
import json
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage
from models.city import City
from models.state import State
timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class TestCity(unittest.TestCase):
    """test class review"""

    def test_subclass(self):
        """tests the subclas basemodel"""
        am = City()
        self.assertIsInstance(am, BaseModel)
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))
        self.assertTrue(hasattr(am, "name"))
        self.assertTrue(hasattr(am, "state_id"))

    def test_attributes(self):
        """test class attritubtes"""
        s_info = City()
        sta_id = State()
        number = sta_id.id
        self.assertEqual(s_info.name, "")
        s_info.name = "New York"
        self.assertEqual(s_info.name, "New York")
        s_info.state_id = number
        self.assertEqual(s_info.state_id, sta_id.id)

    def test__str__(self):
        """test class printing"""
        a = City()
        string = "[City] ({}) {}".format(a.id, a.__dict__)
        self.assertEqual(str(a), string)

    def test_to_dict_amenity(self):
        """test class directory"""
        a = City()
        dicto = a.to_dict()
        self.assertEqual(type(dicto), dict)
        for attribute in a.__dict__:
            self.assertTrue("__class__" in dicto)
            self.assertTrue(attribute in dicto)

    def test_to_dict_values(self):
        """test key/value from dict"""
        a = City()
        a.name = "New York"
        dic = a.to_dict()
        self.assertEqual(dic["created_at"], a.created_at.strftime(timeformat))
        self.assertEqual(dic["updated_at"], a.updated_at.strftime(timeformat))
        self.assertEqual(dic["__class__"], "City")
        self.assertEqual(dic["name"], "New York")

    def test_base_pep8_conformance_City(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)
