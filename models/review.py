#!/usr/bin/python3
"""
Defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review
    Attributes:
        place_id (str)
        user_id (str)
        text (str)
    """
    place_id = ""
    user_id = ""
    text = ""
