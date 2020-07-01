#!/usr/bin/python3
"""Review test module"""
import unittest
import json
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class TestReview(unittest.TestCase):
    """test class review"""

    def test_subclass(self):
        """tests the subclass basemodel"""
        am = Review()
        self.assertIsInstance(am, BaseModel)
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))
        self.assertTrue(hasattr(am, "text"))
        self.assertTrue(hasattr(am, "user_id"))
        self.assertTrue(hasattr(am, "place_id"))
        self.assertEqual(am.place_id, "")
        self.assertEqual(am.user_id, "")
        self.assertEqual(am.text, "")

    def test_attributes(self):
        """test class attritubtes"""
        pl = Place()
        st = State()
        numberplace = pl.id
        numberstate = st.id
        rev = Review()
        self.assertEqual(rev.text, "")
        rev.text = "I think it was a boring space with nothing to offer"
        self.assertEqual(rev.text,
                         "I think it was a boring space with nothing to offer")
        self.assertNotEqual(rev.place_id, pl.id)
        rev.place_id = numberplace
        self.assertEqual(rev.place_id, pl.id)

    def test__str__(self):
        """test class printing"""
        a = Review()
        string = "[Review] ({}) {}".format(a.id, a.__dict__)
        self.assertEqual(str(a), string)

    def test_to_dict_amenity(self):
        """test class directory"""
        a = Review()
        dicto = a.to_dict()
        self.assertEqual(type(dicto), dict)
        for attribute in a.__dict__:
            self.assertTrue("__class__" in dicto)
            self.assertTrue(attribute in dicto)

    def test_to_dict_values(self):
        """test key/value from dict"""
        a = Review()
        pl = Place()
        st = State()
        a.place_id = pl.id
        a.state_id = st.id
        a.text = "nice place"
        dic = a.to_dict()
        self.assertEqual(dic["created_at"], a.created_at.strftime(timeformat))
        self.assertEqual(dic["updated_at"], a.updated_at.strftime(timeformat))
        self.assertEqual(dic["__class__"], "Review")
        self.assertEqual(dic["text"], "nice place")
        self.assertEqual(dic["place_id"], a.place_id)
        self.assertEqual(dic["state_id"], a.state_id)

    def test_base_pep8_conformance_City(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.text.__doc__)
