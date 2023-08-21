#!/usr/bin/python3
"""simple flask app
"""
from flask import Flask, render_template
from models import storage
from models.generator import Generator
app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
  """reload storage after each request
  """
  storage.close()

@app.route("/parts_by_gens", strict_slashes=False)
def parts_gens_list():
  """list gens and parts sorted by name
  """
  gens = list(storage.all(Generator).values())
  gens.sort(key=lambda x: x.name)
  for gen in gens:
    gen.parts.sort(key=lambda x: x.name)
  return render_template('parts_by_gens.html', gens=gens)

if __name__ == "__main__":
  app.run(debug=True)
