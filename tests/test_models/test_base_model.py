#!/usr/bin/python3

import console
from datetime import datetime
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pep8


class TestBaseModel(unittest.TestCase):

    def test_base_pep8_conformance_base_model(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_instances(self):
        instancecreated = BaseModel()
        self.assertIs(type(instancecreated), BaseModel)
        instancecreated.name = "Holberton"
        instancecreated.number = 89
        instance_attributes = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str, "number": int}
        for attributes, typed in instance_attributes.items():
            with self.subTest(attributes=attributes, typed=typed):
                self.assertIn(attributes, instancecreated.__dict__)
                self.assertIs(
                    type(instancecreated.__dict__[attributes]), typed)
        self.assertEqual(instancecreated.name, "Holberton")
        self.assertEqual(instancecreated.number, 89)

    def test_time_attributes(self):
        createdat = datetime.now()
        first_instance = BaseModel()
        updatedat = datetime.now()
        self.assertTrue(createdat <= first_instance.created_at <= updatedat)
        createdat2 = datetime.now()
        second_instance = BaseModel()
        updatedat2 = datetime.now()
        self.assertTrue(createdat2 <= second_instance.created_at <= updatedat2)
        self.assertNotEqual(first_instance.created_at,
                            first_instance.updated_at)
        self.assertNotEqual(second_instance.created_at,
                            second_instance.updated_at)

    def test_id_assignment(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        uuid1 = instance1.id
        uuid2 = instance2.id
        self.subTest(uuid1=uuid1)
        self.subTest(uuid2=uuid2)
        self.assertIs(type(uuid1), str)
        self.assertIs(type(uuid2), str)
        self.assertNotEqual(instance1.id, instance2.id)

    def test_to_dict(self):
        instance1 = BaseModel()
        instance1.name = "Angello"
        instance1.my_number = 35
        dicto = instance1.to_dict()
        dicto_expected = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(dicto.keys(), dicto_expected)
        self.assertEqual(dicto['__class__'], 'BaseModel')
        self.assertEqual(dicto['name'], "Angello")
        self.assertEqual(dicto['my_number'], 35)

    # def test_to_dict_types

    def test__str__(self):
        instance3 = BaseModel()
        example = "[BaseModel] ({}) {}". format(
            instance3.id, instance3.__dict__)
        self.assertEqual(example, str(instance3))
