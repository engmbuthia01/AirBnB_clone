#!/usr/bin/python3
"""defines user class"""

from models.base_model import BaseModel


class User(BaseModel):
    first_name = ""
    last_name = ""
    email = ""
    password = ""
