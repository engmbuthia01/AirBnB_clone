#!/usr/bin/python3
"""
This module defines the base model
defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """parent class"""

    def __init__(self, *args, **kwargs):
       """initializes the newly created objects"""

       self.id = str(uud.uud4())
       self.created_at = datetime.now()
       self.updated_at = datetime.now()
       tformat = "%Y-%m-%dT%H:%M:%S.%f"

       if len(kwargs) != 0:
           for k, v in kwargs.items():
               if k == "created_at" or k == "updated_at":
                   self.__dict__[k] = datetime.strptime(v, tformat)
               else:
                   self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """

        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """String representation of a BaseModel instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))
