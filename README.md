# flaskTask

Basic assignment to get you started with Flask and Python, written in the style of UNSTPB ACS CTI assignments.

## Task

Implement a basic Flask web application and an interactor (which you will use to test your own implementation).

### Flask server

The Flask server should have the following three endpoints:

1. `/` - GET - returns `Hello, World!` when accessed via a GET request.
2. `/name/<name>` - GET - returns `Hello, <name>!` when accessed via a GET request.
3. `/print` - POST, parameter: `data` - returns contents of `data` when accessed via a POST request.

### Interactor

The interactor should be a Python script that accomplishes two things:

1. It sends requests to the Flask server and prints the responses.
2. It sends a request to Google Maps' Geocoding API and prints the response. Use this to find the location of the Ienachita Vacarescu National College. See [this](https://www.geeksforgeeks.org/get-post-requests-using-python/) link for support.

## Setup

Create a Python environment:

```bash
python -m venv env
```

Activate the environment:

```bash
source env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask:

```bash
pip install flask requests
```

To run the app:

```bash
python app.py
```

To run the interactor::

```bash
python interactor.py
```

## Resources

- [Python decorators](https://www.geeksforgeeks.org/decorators-in-python/)
- [Python format strings](https://www.w3schools.com/python/python_strings_format.asp)
- [HTTP methods](https://www.w3schools.com/tags/ref_httpmethods.asp)
- [What JSON is](https://www.w3schools.com/whatis/whatis_json.asp)
- [Get data received in POST request in Flask](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request)
- [What `__name__` == `__main__` does in Python](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)
- [Same as above, but from Stack Overflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
- [Python `requests` library introduction](https://www.geeksforgeeks.org/get-post-requests-using-python/)

## Tooling Documentation

- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Requests](https://requests.readthedocs.io/en/master/)
