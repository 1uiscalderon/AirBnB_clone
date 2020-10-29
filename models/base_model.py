#!/usr/bin/python3
"""
This module will define all common attributes/methods for other classes
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialize class BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        Updates
        """
        self.updated_at = datetime.today()
    
    def to_dict(self):
        """
        Dictionary
        """
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = d["created_at"].isoformat("T")
        d["updated_at"] = d["updated_at"].isoformat("T")
        return d