#!/usr/bin/python3
"""
This class holds the methods for the User and inherits from the BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """This holds the attributes for the User Class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    pass
