#!/usr/bin/python3
"""This contains test methods for the State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state_creation(self):
        """Test state creation"""
        state = State()
        self.assertIsNotNone(state)
        self.assertIsInstance(state, State)

    def test_state_attributes(self):
        """Test state attributes"""
        state = State(name="Test State")
        self.assertEqual(state.name, "Test State")

    def test_state_str_representation(self):
        """Test state str representation"""
        state = State(name="Test State")
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)

    def test_state_to_dict_method(self):
        """Test state to_dict method"""
        state = State(name="Test State")
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['id'], state.id)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], 'Test State')

    def test_state_from_dict_method(self):
        """Test state from_dict method"""
        state_data = {
            'id': '1234',
            '__class__': 'State',
            'name': 'Test State'
        }
        state = State(**state_data)
        self.assertIsInstance(state, State)
        self.assertEqual(state.id, '1234')
        self.assertEqual(state.name, 'Test State')


if __name__ == "__main__":
    unittest.main()
