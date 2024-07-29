#!/usr/bin/python3

"""
This module defines the a class BaseModel
that defines all common attributes/methods
for other classes
"""

import uuid
import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self):
        """Initializing"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation"""
        clsname = self.__class__.__name__
        return ("[{}] ({}) {}".format(clsname, self.id, self.__dict__))

    def save(self):
        """updates, updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary respresentation"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__clas__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return (new_dict)
