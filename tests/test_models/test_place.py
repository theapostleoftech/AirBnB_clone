#!/usr/bin/python3
"""This contains test methods for the Place class"""
import unittest
from models.place import Place
from models.city import City
from models.user import User


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.city = City()
        self.city.save()
        self.user = User()
        self.user.save()

    def tearDown(self):
        """Tear down the test environment"""
        del self.city
        del self.user

    def test_place_creation(self):
        """Test place creation"""
        place = Place()
        self.assertIsNotNone(place)
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        """Test place attributes"""
        place = Place(
            city_id=self.city.id,
            user_id=self.user.id,
            name="Test Place",
            description="Test Description",
            number_rooms=2,
            number_bathrooms=1, max_guest=4,
            price_by_night=100, latitude=1.2345, longitude=5.6789)
        self.assertEqual(place.city_id, self.city.id)
        self.assertEqual(place.user_id, self.user.id)
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "Test Description")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 1.2345)
        self.assertEqual(place.longitude, 5.6789)
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_str_representation(self):
        """Test place str representation"""
        place = Place(
            city_id=self.city.id, user_id=self.user.id, name="Test Place")
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)

    def test_place_to_dict_method(self):
        """Test place to_dict method"""
        place = Place(
            city_id=self.city.id, user_id=self.user.id, name="Test Place")
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['id'], place.id)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['name'], 'Test Place')
        self.assertEqual(place_dict['city_id'], self.city.id)
        self.assertEqual(place_dict['user_id'], self.user.id)

    def test_place_from_dict_method(self):
        """Test place from_dict method"""
        place_data = {
            'id': '1234',
            '__class__': 'Place',
            'name': 'Test Place',
            'city_id': self.city.id,
            'user_id': self.user.id
        }
        place = Place(**place_data)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.id, '1234')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.city_id, self.city.id)
        self.assertEqual(place.user_id, self.user.id)


if __name__ == "__main__":
    unittest.main()
