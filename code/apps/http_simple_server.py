"""
Module http_simple_server

Remarks
-------

This program defines a simple `SimpleHTTPRequestHandler` class that subclasses `BaseHTTPRequestHandler` from the `http.server` module. The `do_GET` method of this class is called whenever the server receives a `GET` request, and it sends a fixed response to the client with a status code of `200 (OK)` and the body "Hello, World!".

To test this server, run the program and then send a GET request to it using a tool such as curl: `curl http://localhost:8000`.

"""

import http.server

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """A simple HTTP request handler that always returns a fixed response."""
    
    def do_GET(self):
        """Handle GET requests."""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

def test_http_server():
    """Test the SimpleHTTPRequestHandler class."""
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Starting HTTP server on port 8000...")
    httpd.serve_forever()

# test_http_server()
