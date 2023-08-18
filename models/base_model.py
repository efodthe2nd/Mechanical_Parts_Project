#!/usr/bin/env python3

"""The base class for project"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from models import storage_type

Base = declarative_base()


class BaseModel:
  """Base class for all models
  Attributes:
    id (sqlalchemy strin): the BaseModel id.
    created_at (sqlalchemy Datetime): The datetime at creation.
    updated_at(sqlalchemy Datetime): the datetime of last update.
  """
  
  id = Column(String(60),
              nullable=False,
              primary_key=True,
              unique=True)

  created_at = Column(DATETIME,
                      nullable=False,
                      default=datetime.utcnow())
  updated_at = Column(DATETIME,
                      nullable=False,
                      default=datetime.utcnow())
  
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
      
      if storage_type == 'db':
        if not hasattr(kwargs, 'id'):
          setattr(self, 'id', str(uuid.uuid4()))
        if not hasattr(kwargs, 'created_at'):
          setattr(self, 'created_at', datetime.today())
        if not hasattr(kwargs, 'updated_at'):
          setattr(self, 'updated_at', datetime.today())


    else:
      self.id = str(uuid.uuid4())
      self.created_at = datetime.today()
      self.updated_at = datetime.today()

  def __str__(self):
    """Return the string representation of the BaseModel class"""
    cls = type(self).__name__
    obj_members = self.__dict__.copy()
    if '_sa_instance_state' in obj_members:
      del obj_members['_sa_instance_state']
    return '[{}] ({}) {{\'name\': \'{}\', \'id\': \'{}\', {}}}'.format(
		  cls,
			self.id,
			obj_members['name'],
 			obj_members['id'],
			', '.join("'{}': {}".format(key, value) for key, value in obj_members.items()
			if key not in ['name', 'id']))

  def save(self):
    """Updates the public instance attributes updated_at """
    import models

    self.updated_at = datetime.today()
    models.storage.new(self)
    models.storage.save()
  
  def to_dict(self):
    """Converts instance into dict format"""
    attr = self.__dict__.copy()
    attr['__class__'] = self.__class__.__name__
    if type(attr['created_at']) is not str:
      attr['created_at'] = attr['created_at'].isoformat()
    if type(attr['updated_at']) is not str:
      attr['updated_at'] = attr['updated_at'].isoformat()
    if '_sa_instance_state' in attr.keys():
      del(attr['_sa_instance_state'])
    return attr

  def delete(self):
    """deletes the current instance from the storage """
    from models import storage
    storage.delete(self)
