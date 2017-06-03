# Socboard Backend
Last updated by Weilon Ying on 3rd June 2017

## busdepartures.py
### Dependencies
* Python 3
    * [requests library](https://pypi.python.org/pypi/requests)
    * [dateutil library](https://pypi.python.org/pypi/python-dateutil])
* A working TfNSW ([Transport for NSW](https://opendata.transport.nsw.gov.au/)) API Key

### Description
Gets departure times from a specific bus stop. Defaults to bus stop 203116 (UNSW High Street near Gate 9) if none provided. Uses TfNSW REST API.
