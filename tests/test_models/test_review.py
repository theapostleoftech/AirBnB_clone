#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel
from models.place import Place
from models.user import User

class TestReviewClass(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up an instance of the Review class for testing.
        """
        self.review = Review()

    def test_is_subclass(self):
        """
        Test if the Review class is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_place_id_attribute(self):
        """
        Test if the place_id attribute exists and is initially an empty string.
        """
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertEqual(self.review.place_id, '')

    def test_user_id_attribute(self):
        """
        Test if the user_id attribute exists and is initially an empty string.
        """
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertEqual(self.review.user_id, '')

    def test_text_attribute(self):
        """
        Test if the text attribute exists and is initially an empty string.
        """
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.text, '')

    def test_place_id_type(self):
        """
        Test if the place_id attribute can be assigned an instance of the Place class.
        """
        self.review.place_id = Place()
        self.assertIsInstance(self.review.place_id, Place)

    def test_user_id_type(self):
        """
        Test if the user_id attribute can be assigned an instance of the User class.
        """
        self.review.user_id = User()
        self.assertIsInstance(self.review.user_id, User)

    def test_text_type(self):
        """
        Test if the text attribute can be assigned a string value.
        """
        self.review.text = 'This is a review'
        self.assertIsInstance(self.review.text, str)

if __name__ == '__main__':
    unittest.main()