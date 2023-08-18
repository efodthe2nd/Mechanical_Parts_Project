#!/usr/bin/python3
"""Test link Many-To-Many Place <> Amenity
"""
import models
from models import *
from models.manufacturer import Manufacturer
from models.generator import Generator
from models.part import Part

#createion of a Manufacturer
manufacturer = Manufacturer(name="Honda2")
manufacturer.save()

#creation of a Generator
generator = Generator(manufacturer_id = manufacturer.id, name="Honda Keyless2")
generator.save()

#creation of parts
part1 = Part(name="Spark Plug", price="N500")
part1.save()
part2 = Part(name="Fuel Tap", price="N700")
part2.save()

#link parts to Gen
generator.parts.append(part1)
generator.parts.append(part2)

storage.save()

print("OK")
