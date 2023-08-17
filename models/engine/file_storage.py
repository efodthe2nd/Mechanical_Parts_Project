#!/usr/bin/env python3
"""File storage class"""

import json
from models.base_model import BaseModel
from models.manufacturer import Manufacturer
from models.generator import Generator
from models.part import Part

class FileStorage:
  """Serializes instances to a json file and deserializes"""

  __file_path = "file.json"
  __objects = {}

  def all(self, cls=None):
    """returns the dictionary __objects"""
    if cls is None:
      return self.__objects
    cls_name = cls.__name__
    dct = {}

    for key in self.__objects.keys():
      if key.split('.')[0] == cls_name:
        dct[key] = self.__objects[key]
    return dct

  def new(self, obj):
    """sets __objects with key"""
    if not obj:
      return
    attr = obj.to_dict()
    key = attr['__class__'] + '.' + attr['id']
    self.__objects[key] = obj

  def save(self):
    """serializes __objects to json file"""
    objs = {}
    for key in self.__objects:
      objs[key] = self.__objects[key].to_dict()
    with open(self.__file_path, "w") as f:
      json.dump(objs, f, indent=4)

  def reload(self):
    """deserializes the json file to __object"""
    try:
      with open(self.__file_path, "r") as f:
        objs = json.loads(f.read())
        for key, obj in objs.items():
          if key not in self.__objects:
            name = obj['__class__']
            base = eval(f"{name}(**obj)")
            self.new(base)
    except Exception:
      pass

  def delete(self, obj=None):
    """deletes the object obj from the attr
       __objects if it's inside it
    """
    if obj is None:
      return
    obj_key = obj.to_dict()['__class__'] + '.' + obj.id
    if obj_key in self.__objects.keys():
      del self.__objects[obj_key]

