import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")

    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_amenity_str(self):
        amenity = Amenity()
        self.assertIsInstance(str(amenity), str)

    def test_amenity_save_method(self):
        amenity = Amenity()
        first_updated_at = amenity.updated_at
        amenity.save()
        second_updated_at = amenity.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_amenity_to_dict_method(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(datetime.fromisoformat(amenity_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(amenity_dict['updated_at']), datetime)


if __name__ == '__main__':
    unittest.main()
