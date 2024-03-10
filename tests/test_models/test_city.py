#!/usr/bin/python3
"""This contains test methods for the City class"""
import unittest
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.state = State()
        self.state.save()

    def tearDown(self):
        """Tear down the test environment"""
        del self.state

    def test_city_creation(self):
        """Test city creation"""
        city = City()
        self.assertIsNotNone(city)
        self.assertIsInstance(city, City)

    def test_city_state_id(self):
        """Test city state_id"""
        city = City(state_id=self.state.id)
        self.assertEqual(city.state_id, self.state.id)

    def test_city_state_instance(self):
        """Test city state instance"""
        city = City(state_id=self.state.id)
        self.assertIsInstance(city.state, State)

    def test_city_str_representation(self):
        """Test city str representation"""
        city = City(state_id=self.state.id, name="Test City")
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)

    def test_city_to_dict_method(self):
        """Test city to_dict method"""
        city = City(state_id=self.state.id, name="Test City")
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['id'], city.id)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['name'], 'Test City')
        self.assertEqual(city_dict['state_id'], self.state.id)

    def test_city_from_dict_method(self):
        """Test city from_dict method"""
        city_data = {
            'id': '1234',
            '__class__': 'City',
            'name': 'Test City',
            'state_id': self.state.id
        }
        city = City(**city_data)
        self.assertIsInstance(city, City)
        self.assertEqual(city.id, '1234')
        self.assertEqual(city.name, 'Test City')
        self.assertEqual(city.state_id, self.state.id)


if __name__ == "__main__":
    unittest.main()
