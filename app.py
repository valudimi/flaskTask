"""
Flask assignment - fill in the TODO sections as described in the task description.
"""

from flask import Flask, request

app = Flask(__name__)


# TODO 1: Add a decorator to the function below that will allow it to be
# accessed at the path '/' (also called the "root" path).
...
def hello_world():
    """
    Root path that returns a string.
    """

    # TODO 2: Return a string that says 'Hello, World!'
    # Note: check what the pass keyword does in Python,
    # and replace it.
    pass

# TODO 3: Add a decorator to the function below that will allow it to be
# accessed at the path '/name/<name>', where <name> is a string that will be
# returned by the function.
...
def hello_name(name):
    """
    Path that returns a string with a name.
    """

    # TODO 4: Return a string that says 'Hello, <name>!'
    # Read up on Python fstrings to see how to insert a variable cleanly.
    return ...

# TODO 5: Add a decorator to the function below that will allow it to be
# accessed at the path '/print', where it will only accept POST requests.
...
def print_post():
    """
    Path that returns a string with a name.
    """

    # TODO 6: Return a string that says 'Data received: <data>', where <data>
    # is the data that was sent in the POST request. Use the request object
    # to get the data.
    data = ...

    return ...

# TODO 7: add main guard
...
