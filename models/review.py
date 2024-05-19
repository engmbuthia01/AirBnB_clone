#!/usr/bin/python3
"""
This module defines a
review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    user_id = ""
    place_id = ""
    text = ""
