#!/usr/bin/python3
"""This class holds the methods for the City Class"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """This holds the attributes for the City Class """
    state_id = State().id
