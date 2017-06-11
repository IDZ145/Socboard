# Socboard Backend
Last updated by Weilon Ying on 11th June 2017

## busdepartures.py
### Dependencies
* Python 3
    * [requests library](https://pypi.python.org/pypi/requests)
    * [dateutil library](https://pypi.python.org/pypi/python-dateutil)
    * [flask](https://flask.pocoo.org)
    * [flask-restful](https://flask-restful.readthedocs.io/en/0.3.5/)
* A working TfNSW ([Transport for NSW](https://opendata.transport.nsw.gov.au/)) API Key

### Description
Handles everything handled on the server-side. Currently serves test data. Functions include:
* Gets departure times from a specific bus stop. Uses TfNSW REST API.
* Handling AJAX requests from frontend.
