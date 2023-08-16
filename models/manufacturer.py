#!/usr/bin/env python3
"""Manufacturer module"""
from models.base_model import BaseModel

class Manufacturer(BaseModel):
  """This class initializes manufacturer instances"""
  name: str = ""
