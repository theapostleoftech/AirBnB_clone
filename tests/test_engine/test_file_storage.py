#!/usr/bin/python3
import unittest
import json as js
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class
    """

    def setUp(self):
        """
        Set up method for the test cases
        """
        self.file_path = FileStorage._FileStorage__file_path
        self.storage = FileStorage()
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """
        Tear down method for the test cases
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """
        Test the all method
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        Test the new method
        """
        model = BaseModel()
        self.storage.new(model)
        obj_key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(obj_key, self.storage.all())

    def test_save(self):
        """
        Test the save method
        """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = js.load(file)
            obj_key = f"{model.__class__.__name__}.{model.id}"
            self.assertIn(obj_key, data)

    def test_reload(self):
        """
        Test the reload method
        """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        obj_key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(obj_key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
