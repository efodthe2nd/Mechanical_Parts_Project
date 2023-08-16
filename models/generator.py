#!/usr/bin/env python3
"""Generator Module"""
from models.base_model import BaseModel

class Generator(BaseModel):
  """This class initializes Generator instances"""
  manufacturer_id: str = ""
  name: str = ""
