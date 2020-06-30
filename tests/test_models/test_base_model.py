#!/usr/bin/python3
"""test module for base model"""

import console
from datetime import datetime
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pep8


class TestBaseModel(unittest.TestCase):
    """Test the basemodel class}
    """

    def test_base_pep8_conformance_base_model(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_instances(self):
        """test instances creation"""
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
        """it tests the attribute of time"""
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
        """it tests the id assignment"""
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
        """tests dictionary instance"""
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

    def test__str__(self):
        """tests the printing"""
        instance3 = BaseModel()
        example = "[BaseModel] ({}) {}". format(
            instance3.id, instance3.__dict__)
        self.assertEqual(example, str(instance3))

    def test_save(self):
        """tests the save instances"""
        instances = BaseModel()
        created_at_old = instances.created_at
        updated_at_old = instances.updated_at
        instances.save()
        created_at_new = instances.created_at
        updated_at_new = instances.updated_at
        self.assertNotEqual(updated_at_old, updated_at_new)
        self.assertEqual(created_at_old, created_at_new)

    def test_base_model_docstring(self):
        """test the docstring of the class"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "base_model.py needs a docstring")

    def test_base_pep8_conformance_base_modeltest(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['/tests_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 1)
