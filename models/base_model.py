#!/usr/bin/python3
"""
This module defines the class
Basemodel
"""

import uuid
from datetime import datetime


class Basemodel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates the updated_at attribute with the
        current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self)
