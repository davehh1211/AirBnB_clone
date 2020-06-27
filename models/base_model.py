#!/usr/bin/python3
"""
    """
from datetime import datetime
import uuid
import models


class BaseModel:
    """[summary]
    """

    def __init__(self, *args, **kwargs):
        if kwargs or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dicto = {'my_number': self.my_number,
                 'name': self.name,
                 '__class__': self.__class__.__name__,
                 'updated_at': self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                 'id': self.id,
                 'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")}
        return dicto

    def __str__(self):
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(self.__dict__)))
