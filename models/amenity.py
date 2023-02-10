#!/usr/bin/python3
"""
importing basemodel 
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Custom amenity class
    Attributes:
        name(str): amenity name
    """
    name = ""
