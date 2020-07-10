#!/usr/bin/python3
"""User test module"""
import unittest
import json
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage
from models.user import User
timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class TestUser(unittest.TestCase):
    """test class User"""

    def test_subclass(self):
        """tests the subclass basemodel"""
        am = User()
        self.assertIsInstance(am, BaseModel)
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))
        self.assertTrue(hasattr(am, "first_name"))
        self.assertTrue(hasattr(am, "last_name"))
        self.assertTrue(hasattr(am, "password"))
        self.assertTrue(hasattr(am, "email"))

    def test_attributes(self):
        """test class attritbutes"""
        user_info = User()
        self.assertEqual(user_info.first_name, "")
        user_info.first_name = "David"
        self.assertEqual(user_info.first_name, "David")
        user_info.last_name = "Villegas"
        self.assertEqual(user_info.last_name, "Villegas")
        user_info.password = "f**ck/"
        self.assertEqual(user_info.password, "f**ck/")
        user_info.email = "villedave@gmail.com"
        self.assertEqual(user_info.email, "villedave@gmail.com")

    def test__str__(self):
        """test class printing"""
        a = User()
        string = "[User] ({}) {}".format(a.id, a.__dict__)
        self.assertEqual(str(a), string)

    def test_to_dict_user(self):
        """test class directory"""
        a = User()
        dicto = a.to_dict()
        self.assertEqual(type(dicto), dict)
        for attribute in a.__dict__:
            self.assertTrue("__class__" in dicto)
            self.assertTrue(attribute in dicto)

    def test_to_dict_values(self):
        """test key/value from dict"""
        a = User()
        dic = a.to_dict()
        self.assertEqual(dic["created_at"], a.created_at.strftime(timeformat))
        self.assertEqual(dic["updated_at"], a.updated_at.strftime(timeformat))
        self.assertEqual(dic["__class__"], "User")

    def test_base_pep8_conformance_user(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.password.__doc__)
