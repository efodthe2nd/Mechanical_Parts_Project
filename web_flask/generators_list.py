#!/usr/bin/python3
"""
Flask module to run the web application and render
on /state_list.
"""
from models import storage
from models.generator import Generator
from flask import Flask, render_template

app = Flask(__name__)

@app.teardown_appcontext
def close_session(exception=None):
    """Close the current session."""
    storage.close()

@app.route('/generator_lists', strict_slashes=False)
def list_state():
    """Render list of all states."""
    generator_list = storage.all(Generator)
    return render_template('generator_list.html', generators=generator_list)

if __name__ == '__main__':
    app.run(debug=True)