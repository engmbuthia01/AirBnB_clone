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

if __name__ == "__main__"
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
