#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """this class will name the amenity given"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
