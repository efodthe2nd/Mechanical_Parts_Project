#!/usr/bin/python3
"""simple flask app
"""
from flask import Flask, render_template
from models import storage
from models.generator import Generator
from os import environ as env
app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
  """reload storage after each request
  """
  storage.close()

@app.route("/generators/<id>", strict_slashes=False)
@app.route("/generators", strict_slashes=False)
def generators_parts_list(id=None):
  """show generator and parts if id is given
  otherwise list all generators
  """
  generators = storage.all(Generator)
  if id:
    generator = generators.get('Generator.{}'.format(id))
    generators = [generator] if generator else []
  else:
    generators = list(generators.values())
  generators.sort(key=lambda x: x.name)
  for generator in generators:
    generator.parts.sort(key=lambda x: x.name)
  return render_template(
    'generators.html',
    generators=generators,
    len=len(generators),
    id=id
  )

if __name__ == "__main__":
  app.run(debug=True)
