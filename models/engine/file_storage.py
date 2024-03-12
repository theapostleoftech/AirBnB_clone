#!/usr/bin/python3
"""This contains modules for the FileStorage"""
import json as js


class FileStorage:
    """This class is responsible for serializing
    instances to a JSON file and deserializes
    JSON file to instance."""

    __file_path = "file.json"
    __objects = {}

    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # FILE_NAME = "data/storage.json"

    # def __init__(self):
    #     """This initializes the FileStorage class"""
    #     self.__file_path = "storage.json"
    #     self.__objects = {}

    def all(self):
        """This returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
               Sets the `obj` with the key `<obj class name>.id
               Args:
                   obj: The object to be added to `__objects`.
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj
        pass

    def save(self):
        """This serializes __objects to the JSON file path"""
        serialized_data = {}
        for key, value in FileStorage.__objects.items():
            serialized_data[key] = value.to_dict()

        with open(FileStorage.__file_path, "w",
                  encoding="utf-8") as write_jsonfile:
            js.dump(serialized_data, write_jsonfile)

    def classes(self):
        """This method returns a dictionary of all the classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """This deserializes the JSON file to __objects if it exists;
        and does nothing if it does not exist."""
        try:
            with open(FileStorage.__file_path, "r",
                      encoding="utf-8") as read_jsonfile:
                deserialized_data = js.load(read_jsonfile)
                for key, value in deserialized_data.items():
                    class_name, obj_id = key.split(".")
                    obj = self.classes().get(class_name)
                    if obj:
                        FileStorage.__objects[key] = obj(**value)

        except FileNotFoundError:
            pass