#!/usr/bin/python3
"""This class contains the methods for the Place Class"""

from models.base_model import BaseModel
from models.city import City
from models.user import User


class Place(BaseModel):
    """This holds the attributes for the Place Class """
    city_id = City().id
    user_id = User().id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = list(str())

    pass
