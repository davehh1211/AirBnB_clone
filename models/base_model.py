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
        #self.updated_at = datetime.now()
        self.name = name
        self.my_number = my_number

    print(id)
    # id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now()
    # @property
    # def name(self):
    #   return self.name

    # @name.setter
    # def name(self, value):
    #    if type(value) is not str:
    #        raise TypeError("{} is not a string".format(value))
    #    if value is None:
    #        raise ValueError("Name must be given")
    #    self.name = value

    # @property
    # def my_number(self):
    #    return self.my_number

    # @my_number.setter
    # def my_number(self, value):
    #    if type(value) is not int:
    #        raise TypeError("{} is not an integer".format(value))
    #   if value is None:
    #       raise ValueError("Number must be given")
    #    self.my_number = value

    def save(self):
        now = datetime.now()
        self.updated_at = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return self.updated_at

    def to_dict(self):
        dicto = {'my_number': self.my_number,
                 'name': self.name,
                 '__class__': self.__class__,
                 'updated_at': self.updated_at,
                 'id': self.id,
                 'created_at': self.created_at}
        return dicto

    def __str__(self):
        return ("[<class name>] (<self.id>) <self.__dict__>".format(self.__class__, self.id, self.__dict__))
