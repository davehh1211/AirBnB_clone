#!/usr/bin/python3
"""
    """
from datetime import datetime
import uuid


class BaseModel:
    """[summary]
    """

    def __init__(self, name=None, my_number=0):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()  # strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now()
        self.name = name
        self.my_number = my_number

    def save(self):
        self.updated_at = datetime.now()

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
