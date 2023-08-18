#!/usr/bin/env python3
"""Part Module"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Part(BaseModel, Base):
  """This Part Class, contains Generator ID, price and name """
  __tablename__ = 'parts'
  if storage_type == 'db':
    name = Column(String(128), nullable=False)
    price = Column(String(60), nullable=False)
    generator_parts = relationship('Generator', 
                                   secondary="generator_part",
                                   backref='generators',
                                   overlaps="generator_parts, generators")

  else:
    name = ""
    price = ""
