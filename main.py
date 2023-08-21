!/usr/bin/python3
"""
Test parts access from a Generator
"""
from models import storage
from models.generator import Generator
from models.part import Part

"""
Objects creations
"""
generator_1 = Generator(name="Friday")
print("New generator: {}".format(generator_1))
generator_1.save()
generator_2 = Generator(name="Saturday")
print("New generator: {}".format(generator_2))
generator_2.save()

part_1_1 = Part(generator_id=generator_1.id, name="wire")
print("new part: {} in the generator: {}".format(part_1_1, generator_1))
part_1_1.save()
part_1_2 = Part(generator_id=generator_1.id, name="wire frame")
print("New part: {} in the generator: {}".format(part_1_2, generator_1))
part_1_2.save()

"""
Verification
"""
print("")
all_gens = storage.all(Generator)
for generator_id, generator in all_gens.items():
  for part in generator.parts:
    print("Find the part {} in the Gen {}".format(part, generator))
