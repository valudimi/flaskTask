"""
Basic interactor to test the functionality of the Flask server.
"""

import requests as re

URL = "http://127.0.0.1:5000"

def test_hello_world():
    """
    Test the root path.
    """

    # TODO 1: Send a GET request to the root path of the server.
    return

def test_hello_name(name):
    """
    Test the /name path.
    """

    # TODO 2: Send a GET request to the /name/<name> path of the server.
    return

def test_print_post(data):
    """
    Test the /print path with a POST request.
    """

    # TODO 3: Send a POST request to the /print path of the server.
    return

# TODO 5: Create a new function that sends a request to the Google Maps API to get
# the latitude and longitude of a location. The function should take the location
# as a parameter and return the latitude and longitude as a tuple.
# Use this to find the location of the Ienachita Vacarescu National College.

# TODO 4: Add a main guard and call the test functions.
