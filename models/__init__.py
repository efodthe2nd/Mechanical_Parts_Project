#!/usr/bin/env python3
"""This module chooses storage"""

from os import getenv

storage_type = getenv('MECH_TYPE_STORAGE')

if storage_type == 'db':
  from models.engine.db_storage import DBStorage
  storage = DBStorage()

else:
  from models.engine.file_storage import FileStorage
  storage = FileStorage()

storage.reload()
