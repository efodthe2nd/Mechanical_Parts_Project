#!/usr/bin/env python3

"""The base class for project"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from models import storage_type

Base = declarative_base()


class BaseModel:
  """This class implements common attributes for other models"""

  def __init__(self, *args, **kwargs):
    """Initializing the instances"""
    if kwargs:
      attr = kwargs.copy()
      if 'created_at' in attr:
        del attr['__class__']
        str_c_at = attr['created_at']
        attr['created_at'] = datetime.strptime(str_c_at, '%Y-%m-%dT%H:%M:%S.%f')
        str_u_at = attr['updated_at']
        attr['updated_at'] = datetime.strptime(str_u_at, '%Y-%m-%dT%H:%M:%S.%f')

      else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

      for key in attr:
        setattr(self, key, attr[key])

    else:
      self.id = str(uuid.uuid4())
      self.created_at = datetime.today()
      self.updated_at = datetime.today()
    
    models.storage.new(self)

  def __str__(self):
    """Return the string representation of the BaseModel class"""
    return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

  def save(self):
    """Updates the public instance attributes updated_at """
    self.updated_at = datetime.today()
    models.storage.save()
  
  def to_dict(self):
    """Returns a dictionary representation of BaseModel"""
    attr = self.__dict__.copy()
    attr['__class__'] = self.__class__.__name__
    if type(attr['created_at']) is not str:
      attr['created_at'] = attr['created_at'].isoformat()
    if type(attr['updated_at']) is not str:
      attr['updated_at'] = attr['updated_at'].isoformat()
    return attr
