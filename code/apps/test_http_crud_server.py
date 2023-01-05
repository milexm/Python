"""
Module test_http_crud_server.py

This code is intended to test a CRUD (Create, Read, Update, Delete) HTTP server.
It does so by sending a GET, POST, PUT, and DELETE request to the server at the
specified URL ('http://localhost:8000') and then checking the response to each
request to ensure that it is correct. If the response is as expected, it is
printed to the console. If any of the assertions fail, an assertion error will
be raised.

"""

import requests

def test_http_crud_server():
    """
    Test the CRUD HTTP server by sending a GET, POST, PUT, and DELETE request and checking the response.
    """
    # Send a GET request
    r = requests.get('http://localhost:8000')
    assert r.text == 'You have sent a GET request.'
    print(f'Request: {r.text}') 

    # Send a POST request
    r = requests.post('http://localhost:8000')
    assert r.text == 'You have sent a POST request.'
    print(f'Request: {r.text}') 

    # Send a PUT request
    r = requests.put('http://localhost:8000')
    assert r.text == 'You have sent a PUT request.'
    print(f'Request: {r.text}')

    # Send a DELETE request
    r = requests.delete('http://localhost:8000')
    assert r.text == 'You have sent a DELETE request.'
    print(f'Request: {r.text}')

if __name__ == '__main__':
    test_http_crud_server()
