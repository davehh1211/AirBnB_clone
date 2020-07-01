#!/usr/bin/python3
"""Place test module"""
import unittest
import json
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class TestPlace(unittest.TestCase):
    """test class place"""

    def test_subclass(self):
        """test subclass basemodel"""
        a = Place()
        self.assertIsInstance(a, BaseModel)
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))

    def test_city_id(self):
        """test city attri"""
        a = Place()
        self.assertTrue(hasattr(a, "city_id"))
        self.assertEqual(a.city_id, "")
        a.city_id = "NewYork255"
        self.assertEqual(a.city_id, "NewYork255")

    def test_user_id(self):
        """test user attri"""
        a = Place()
        self.assertTrue(hasattr(a, "user_id"))
        self.assertEqual(a.user_id, "")
        a.user_id = "100826398757"
        self.assertEqual(a.user_id, "100826398757")

    def test_name(self):
        """test name attri"""
        a = Place()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")
        a.name = "Montauk"
        self.assertEqual(a.name, "Montauk")

    def test_description(self):
        """test description attri"""
        a = Place()
        self.assertTrue(hasattr(a, "description"))
        self.assertEqual(a.description, "")
        a.description = "location at the beach with view to the sea"
        self.assertEqual(a.description,
                         "location at the beach with view to the sea")

    def test_number_rooms(self):
        """test number of rooms attri"""
        a = Place()
        self.assertTrue(hasattr(a, "number_rooms"))
        self.assertEqual(a.number_rooms, 0)
        a.number_rooms = 255
        self.assertEqual(a.number_rooms, 255)

    def test_number_barthrroms(self):
        """test number of bathrooms attri"""
        a = Place()
        self.assertTrue(hasattr(a, "number_bathrooms"))
        self.assertEqual(a.number_bathrooms, 0)
        a.number_bathrooms = 5
        self.assertEqual(a.number_bathrooms, 5)

    def test_max_guest(self):
        """test maximun of guests attri"""
        a = Place()
        self.assertTrue(hasattr(a, "max_guest"))
        self.assertEqual(a.max_guest, 0)
        a.max_guest = 5
        self.assertEqual(a.max_guest, 5)

    def test_price_by_night(self):
        """test price by night attri"""
        a = Place()
        self.assertTrue(hasattr(a, "price_by_night"))
        self.assertEqual(a.price_by_night, 0)
        a.price_by_night = 3500
        self.assertEqual(a.price_by_night, 3500)

    def test_latitude(self):
        """test latitude attri"""
        a = Place()
        self.assertTrue(hasattr(a, "latitude"))
        self.assertIs(type(a.latitude), float)
        self.assertEqual(a.latitude, 0.0)
        a.latitude = 3.6
        self.assertEqual(a.latitude, 3.6)

    def test_longitude(self):
        """test longitude attri"""
        a = Place()
        self.assertTrue(hasattr(a, "longitude"))
        self.assertIs(type(a.longitude), float)
        self.assertEqual(a.longitude, 0.0)
        a.longitude = 3.6
        self.assertEqual(a.longitude, 3.6)

    def test_amenity_ids(self):
        """test amenity attri"""
        a = Place()
        self.assertTrue(hasattr(a, "amenity_ids"))
        self.assertEqual(a.amenity_ids, [])
        a.amenity_ids = ["225LU", "FER82", "ROOT36"]
        self.assertEqual(a.amenity_ids,
                         ["225LU", "FER82", "ROOT36"])

    def test__str__(self):
        """test printing format"""
        a = Place()
        string = "[Place] ({}) {}".format(a.id, a.__dict__)
        self.assertEqual(str(a), string)

    def test_to_dict_amenity(self):
        """test directory method"""
        a = Place()
        dicto = a.to_dict()
        self.assertEqual(type(dicto), dict)
        for attribute in a.__dict__:
            self.assertTrue("__class__" in dicto)
            self.assertTrue(attribute in dicto)

    def test_to_dict_values(self):
        """tests key/value serialization"""
        a = City()
        a.city_id = "NewYork255"
        a.user_id = "100826398757ABBA"
        a.name = "Montauk"
        a.description = "location at the beach"
        a.number_rooms = 255
        a.number_bathrooms = 2
        a.max_guest = 5
        a.price_by_night = 3500
        a.latitude = 3.6
        a.longitude = 5.8
        a.amenity_ids = ["225LU", "FER82", "ROOT36"]
        dic = a.to_dict()
        self.assertEqual(dic["created_at"],
                         a.created_at.strftime(timeformat))
        self.assertEqual(dic["updated_at"],
                         a.updated_at.strftime(timeformat))
        self.assertEqual(dic["__class__"], "City")
        self.assertEqual(dic["city_id"], "NewYork255")
        self.assertEqual(dic["user_id"], "100826398757ABBA")
        self.assertEqual(dic["name"], "Montauk")
        self.assertEqual(dic["description"], "location at the beach")
        self.assertEqual(dic["number_rooms"], 255)
        self.assertEqual(dic["number_bathrooms"], 2)
        self.assertEqual(dic["max_guest"], 5)
        self.assertEqual(dic["price_by_night"], 3500)
        self.assertEqual(dic["latitude"], 3.6)
        self.assertEqual(dic["longitude"], 5.8)
        self.assertEqual(dic["amenity_ids"],
                         ["225LU", "FER82", "ROOT36"])

    def test_base_pep8_conformance_City(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/place.py'])
        self.assertEqual(result.total_errors, 0)
