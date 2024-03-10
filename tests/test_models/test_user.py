#!/usr/bin/python3
"""This contains test methods for the User"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def test_user_attributes(self):
        """Tests the attributes of the User class"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_inheritance(self):
        """Tests if User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attribute_types(self):
        """Tests the types of the User attributes"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_attribute_assignment(self):
        """Tests assigning values to User attributes"""
        user = User()
        user.email = "airbnb1@example.com"
        user.password = "password123"
        user.first_name = "Betty"
        user.last_name = "ALX"
        self.assertEqual(user.email, "airbnb1@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "Betty")
        self.assertEqual(user.last_name, "ALX")


if __name__ == "__main__":
    unittest.main()
