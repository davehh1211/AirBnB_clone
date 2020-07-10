#!/usr/bin/python3
"""module to create a city"""
from models.base_model import BaseModel


class City(BaseModel):
    """this class will create a city and its id"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
