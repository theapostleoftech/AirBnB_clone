#!/usr/bin/python3
"""This class contains the methods for the Review Class"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """This holds the attributes for the Review Class """
    place_id = Place().id
    user_id = User().id
    text = ""
    pass
