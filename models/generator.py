#!/usr/bin/env python3
"""Generator Module"""
from models.base_model import BaseModel, Base
from models import storage_type
from models.part import Part
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Generator(BaseModel, Base):
  """Generator class / table model """
  __tablename__ = 'generators'
  if storage_type == 'db':
    name = Column(String(128), nullable=False)
    manufacturer_id = Column(String(60), ForeignKey('manufacturers.id'), nullable=False)
    parts = relationship('Part', backref='part',
                         cascade='all, delete, delete-orphan')
  else:
    name = ""
    manufacturer_id = ""
