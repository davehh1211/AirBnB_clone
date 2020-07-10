#!/usr/bin/python3
"""State test module"""
import unittest
import json
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage
from models.state import State
timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class TestState(unittest.TestCase):
    """test class state"""

    def test_subclass(self):
        """tests the subclass basemodel"""
        am = State()
        self.assertIsInstance(am, BaseModel)
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))
        self.assertTrue(hasattr(am, "name"))

    def test_attributes(self):
        """test class attritbutes"""
        s_info = State()
        self.assertEqual(s_info.name, "")
        s_info.name = "Ohio"
        self.assertEqual(s_info.name, "Ohio")

    def test__str__(self):
        """test class printing"""
        a = State()
        string = "[State] ({}) {}".format(a.id, a.__dict__)
        self.assertEqual(str(a), string)

    def test_to_dict_state(self):
        """test class directory"""
        a = State()
        dicto = a.to_dict()
        self.assertEqual(type(dicto), dict)
        for attribute in a.__dict__:
            self.assertTrue("__class__" in dicto)
            self.assertTrue(attribute in dicto)

    def test_to_dict_values(self):
        """test key/value from dict"""
        a = State()
        dic = a.to_dict()
        self.assertEqual(dic["created_at"], a.created_at.strftime(timeformat))
        self.assertEqual(dic["updated_at"], a.updated_at.strftime(timeformat))
        self.assertEqual(dic["__class__"], "State")

    def test_base_pep8_conformance_state(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_state(self):
        """test docstring in the file"""
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.name.__doc__)
