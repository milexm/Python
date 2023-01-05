"""
Module http_crud_server.py

Remarks
-------

This code defines a simple CRUD HTTP server using the BaseHTTPRequestHandler class from the Python Standard Library's http.server module. The CRUDHandler class is a subclass of BaseHTTPRequestHandler and overrides the following methods to handle different HTTP requests:

- `do_GET`: handles GET requests
- `do_POST`: handles POST requests
- `do_PUT`: handles PUT requests
- `do_DELETE`: handles DELETE requests
Each of these methods sends a response to the client with a 200 status code and a message indicating the type of request that was received.

The run_server function sets up the server and starts it running on the specified port (default is 8000). The server will run indefinitely until it is stopped manually.

To start the server, you can run the script from the command line:

`python http_crud_server.py`

Once the server is running, you can test it using the test_http_crud_server function provided in the previous code snippet.

"""

from http.server import HTTPServer, BaseHTTPRequestHandler

class CRUDHandler(BaseHTTPRequestHandler):
    """
    A simple CRUD HTTP server that handles GET, POST, PUT, and DELETE requests.
    """

    def do_GET(self):
        """
        Handles GET requests.
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'You have sent a GET request.')

    def do_POST(self):
        """
        Handles POST requests.
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'You have sent a POST request.')

    def do_PUT(self):
        """
        Handles PUT requests.
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'You have sent a PUT request.')

    def do_DELETE(self):
        """
        Handles DELETE requests.
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'You have sent a DELETE request.')

def run_server(server_class=HTTPServer, handler_class=CRUDHandler, port=8000):
    """
    Runs the server on the specified port.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
