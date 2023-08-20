#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.part import Part

fs = FileStorage()

# All Parts
all_parts = fs.all(Part)
print("All Parts: {}".format(len(all_parts.keys())))
for part_key in all_parts.keys():
  print(all_parts[part_key])

print("############################################")

# Create a new Part
new_part = Part()
new_part.name = "Valve Plate"
fs.new(new_part)
fs.save()
print("New Part: {}".format(new_part))

print("############ All Parts #####################")

all_parts = fs.all(Part)
print("All Parts: {}".format(len(all_parts.keys())))
for part_key in all_parts.keys():
  print(all_parts[part_key])

print("############### Delete new Part ##########")
fs.delete(new_part)

all_parts = fs.all(Part)
print("All Parts: {}".format(len(all_parts.keys())))
for part_key in all_parts.keys():
  print(all_parts[part_key])
