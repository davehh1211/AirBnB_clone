#!/usr/bin/python3
"""Module Base of instanciation of a class
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """initialization of base model"""
        if kwargs or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """class that saves instance attribute to a json file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates a dictionary containing
        all keys and values
        """
        dicto = self.__dict__.copy()
        dicto['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dicto['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dicto['__class__'] = self.__class__.__name__
        return dicto

    def __str__(self):
        """print representation of the id of an instance"""
        obj_dict = self.__dict__
        obj_dict.pop("__class__")
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(obj_dict)))
