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
