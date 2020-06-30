#!/usr/bin/python3

import console
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pep8


class TestConsole(unittest.TestCase):

    def test_base_pep8_conformance_console(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    # def test_base_pep8_conformance_consoletest(self):
    #     """Test that we conform to PEP8."""
    #     pep8style = pep8.StyleGuide(quiet=True)
    #     result = pep8style.check_files(['/tests/test_console.py'])
    #     self.assertEqual(result.total_errors, 0)
