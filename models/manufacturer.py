#!/usr/bin/env python3
"""Manufacturer module"""
from models.base_model import BaseModel, Base
from models import storage_type
from models.generator import Generator
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Manufacturer(BaseModel, Base):
  """This class initializes manufacturer instances"""
  __tablename__ = 'manufacturers'
  if storage_type == 'db':
    name = Column(String(128), nullable=False)
    generators = relationship('Generator', backref='manufacturer',
                              cascade='all, delete, delete-orphan')
  else:
    name: str = ""

    @property
    def generators(self):
      '''returns the list of Generator instances with Manufacturer_id
         equals the current Generator.id
         FileStorage relationship between Manufacturer and Generator
      '''
      from models import storage
      related_generators = []
      generators = storage.all(Generator)
      for generator in generators.values():
        if generator.manufacturer_id == self.id:
          related_generators.append(generator)
      return related_generators
