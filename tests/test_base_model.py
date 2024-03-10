#!/usr/bin/python3
"""This conatains unittest files for the BaseModel"""
import unittest

from models.base_model import BaseModel
from models import storage


class BaseModelTest(unittest.TestCase):
    """This contains modules for unit testing of the BaseModel Class"""

    def setUp(self):
        """This sets the fixtures for the tests"""
        self.my_model = BaseModel()

    def tearDown(self) -> None:
        """ This removes the fixtures for the tests"""
        storage.reload()

    def test_base_model_init(self):
        """This tests the __init__ method of the BaseModel class"""
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))

    def test_base_model_to_dict(self):
        """This tests the to_dict method of the BaseModel class"""
        my_model_dict = self.my_model.to_dict()
        my_model_json = BaseModel(**my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertTrue(isinstance(my_model_dict, dict))
        self.assertEqual(my_model_dict['id'], my_model_json.id)

    def test_base_model_save(self):
        """This tests the save method of the BaseModel class"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertEqual(self.my_model.updated_at, old_updated_at)

    def test_base_model_str(self):
        str_result = f"[BaseModel]" \
                     f" ({self.my_model.id}) " \
                     f"{self.my_model.__dict__}"
        self.assertEqual(str(self.my_model), str_result)


if __name__ == "__main__":
    unittest.main()
