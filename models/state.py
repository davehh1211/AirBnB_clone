#!/usr/bin/python3
"""module state"""
from models.base_model import BaseModel


class State(BaseModel):
    """class to create a state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
