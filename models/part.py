#!/usr/bin/env python3
"""Part Module"""
from models.base_model import BaseModel

class Part(BaseModel):
  """This class initializes Part instances"""
  generator_id: str = ""
  name: str = ""
  price: str = ""
