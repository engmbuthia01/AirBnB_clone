#!/usr/bin/python3

"""
This module defines the a class BaseModel
that defines all common attributes/methods
for other classes
"""

import models
import uuid
import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialization"""

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            tform = "%Y-%m-%dT%H:%M:%S.%f"

            if len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "created_at" or k == "updated_at":
                        self.__dict__[k] = datetime.strptime(v, tform)
                    else:
                        self.__dict__[k] = v

    def __str__(self):
        """string representation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))


    def save(self):
        """updates, updated_at with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """dictionary respresentation"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__clas__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return (new_dict)
