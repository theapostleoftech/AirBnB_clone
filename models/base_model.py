#!/usr/bin/python3

"""This is contains the Base class for the AirBnB_clone project"""

import uuid
from datetime import datetime as dt

import models


class BaseModel:
    """
    This class is the base class for all other classes in the application.
    It provides a unique identifier, creation and update timestamps, and
    methods for converting the object to and from a dictionary.
    """

    def __init__(self, *args, **kwargs):
        """
                Instantiation of the BaseModel class.

                Args:
                    *args: Unused positional arguments.
                    **kwargs: Key-value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, dt.strptime
                                (value, '%Y-%m-%dT%H:%M:%S.%f'))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

    def __str__(self):
        """This function prints the class name, id, and dictionary items"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """This function updates updated_at with the current datetime"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """This function returns a dictionary containing keys/values
        of __dict__ of the instance"""

        dict_data = self.__dict__.copy()
        dict_data['__class__'] = self.__class__.__name__
        dict_data['created_at'] = self.created_at.isoformat()
        dict_data['updated_at'] = self.updated_at.isoformat()
        return dict_data
