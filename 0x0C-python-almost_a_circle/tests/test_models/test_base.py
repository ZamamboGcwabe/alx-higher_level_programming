#!/usr/bin/python3
"""Tests the Base function."""


import unittest
from base import Base


class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        """Test if id is assigned correctly"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(5)
        self.assertEqual(b2.id, 5)

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_data(self):
        """Test to_json_string with data"""
        data = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]
        result = Base.to_json_string(data)
        expected_result = '[{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]'
        self.assertEqual(result, expected_result)

    def test_save_to_file_empty(self):
        """Test save_to_file with empty list"""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_data(self):
        """Test save_to_file with data"""
        data = [Base(3), Base(4)]
        Base.save_to_file(data)
        with open("Base.json", "r") as f:
            content = f.read()
        expected_content = '[{"id": 3}, {"id": 4}]'
        self.assertEqual(content, expected_content)

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string"""
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_data(self):
        """Test from_json_string with data"""
        data = '[{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]'
        result = Base.from_json_string(data)
        expected_result = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]
        self.assertEqual(result, expected_result)

    def test_create(self):
        """Test create method"""
        d1 = {"id": 5, "name": "New object"}
        instance = Base.create(**d1)
        self.assertEqual(instance.id, 5)
        self.assertEqual(instance.name, "New object")

    # Add more tests to cover other methods and functionalities


if __name__ == "__main__":
    unittest.main()

