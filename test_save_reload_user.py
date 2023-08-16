#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.manufacturer import Manufacturer

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
  obj = all_objs[obj_id]
  print(obj)

print("-- Create a new Manufacturer --")
my_manufacturer = Manufacturer()
my_manufacturer.name = "Sumec"
my_manufacturer.save()
print(my_manufacturer)

print("-- Create another Manufacturer 2 ----")
my_man2 = Manufacturer()
my_man2.name = "Elepaq"
my_man2.save()
print(my_man2)
