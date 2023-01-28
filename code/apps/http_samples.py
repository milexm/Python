''' 
Module http_samples.py

Remarks
------
This module contains the following auxiliary classes: `SimpleRequestHandler` and
`CRUDRequestHandler`. The first class creates a simple HTTP handler which
handles just the `GET` request. The second, instead, handles all the `CRUD`
requests.  In both cases, the seervers and the clients run in different threads.
This is to allow servers and clients to run in parallel so the clients can issue
their requests to the related servers.  When the clients finish their task, the
related threads terminate.  On the other hand, because the servers run in an
endless loop, the related threads must be shutdown from outside so the loop
terminates and the control goes back to the `http_menu.py` module.    
'''
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from http.client import HTTPConnection
from time import sleep
import requests

class SimpleRequestHandler(BaseHTTPRequestHandler):
    '''  
    This class defines a `SimpleHTTPRequestHandler` that
    subclasses `BaseHTTPRequestHandler` from the `http.server` module. The
    `do_GET` method is called whenever the server receives a `GET` request, and it sends a fixed response to the client with a status
    code of `200 (OK)` and the body "Hello, World!".

    '''

    def _send_response(self, message):
        """
        Echoes back the message sent by the client.
        
        Parameters
        ----------
        message : str 
            The message sent by the client end echoed back by the server.
  
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        """
        Handles the `GET` requests
        """
        message = "Hello, World!"
        self._send_response(message)

class CRUDRequestHandler(BaseHTTPRequestHandler):
    """
    This class defines a `CRUDRequestHandler` that subclasses
    `BaseHTTPRequestHandler` from the `http.server` module. 
    The CRUDHandler class is a subclass of BaseHTTPRequestHandler and overrides the following methods to handle different HTTP requests:

    - `do_GET`: handles GET requests
    - `do_POST`: handles POST requests
    - `do_PUT`: handles PUT requests
    - `do_DELETE`: handles DELETE requests

    Each of these methods sends a response to the client with a 200 status code and a message indicating the type of request that was received.
      
    """

    def do_GET(self):
        """
        Handles `GET` requests.
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'You have sent a GET request.')

    def do_POST(self):
        """
        Handles `POST` requests.
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'You have sent a POST request.')

    def do_PUT(self):
        """
        Handles `PUT` requests.
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'You have sent a PUT request.')

    def do_DELETE(self):
        """
        Handles `DELETE` requests.
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'You have sent a DELETE request.')

    
class HttpSamples:

    def __init__(self):
        ''' Initialize the class `HttpSAmples` instance. '''
        self.server_address = ("localhost", 8000)
        self.server = None
        self.host = "localhost"
        self.port = 8000
      
    # **** Simple server **** 

    # Run simple server.
    def run_simple_server(self):
        """
        Starts the HTTP simple server. 
        
        Remarks
        -----=
        This function runs in a thread until the thread is terminated by the `simple_http_server` calling function. 

        """
        self.server = HTTPServer(self.server_address, SimpleRequestHandler)
        self.server.serve_forever()
      

    # Run simple client. 
    def run_simple_client(self):
        """
        Issues a `GET` request to the server, retrieves the response from the server, and displays it.  

        Remarks
        -----=
        This function runs in a thread until it completes its task and the thread is terminated. 

        """
        conn = HTTPConnection(self.host, self.port)
        conn.request('GET', '/')
        response = conn.getresponse()
        print(response.read().decode())
        

    def simple_http_server(self):
        """
        Starts the server and client threads.   

        Remarks
        -----=
        This function sets a delay of 3 sec to allow the client thread 
        to print to the console the response from the server.

        It also execute a while loop waiting for the client thread to terminate. If you change the delay, to 2 sec for example, the message `Client thread still running` is displayed several times until the client thread terminates. 
        
        After that the function terminate the server thread shutting its forever loop, so allowing the control to go back to the `http_menu.py` module.   

        """

        server_thread = Thread(target=self.run_simple_server) 
        server_thread.start()  
        client_thread = Thread(target=self.run_simple_client)
        client_thread.start()
        
        # This delay is to allow the client thread 
        # to print to the console. 
        sleep(3)

        while client_thread.is_alive():
            # To experiment: print this in a loop by 
            # setting the sleep time to 2 seconds.
            print('Client thread still running')
        
        print('Client thread completed. Terminate the server thread also.  ')
        # Terminate the server thread. 
        self.server.shutdown()
        
        
    # **** CRUD server **** 

    # Run CRUD server.
    def run_crud_server(self):
        """
        Starts the HTTP CRUD server. 
        
        Remarks
        -----=
        This function runs in a thread until the thread is terminated by the `crud_http_server` calling function. 

        """
        self.server = HTTPServer(self.server_address, CRUDRequestHandler)
        print(f'Starting HTTP CRUD server on port 8000...')
        self.server.serve_forever()
       
    # Run CRUD client. 
    def run_crud_client(self):
        """
        Issues a `CRUD` requests to the server, retrieves the response from the server, and displays them.  

        Remarks
        -----
        This function runs in a thread until it completes its task and the thread is terminated. 

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

        
    def crud_http_server(self):
        """
        Starts the server and client threads.   

        Remarks
        -----
        This function sets a delay of 10 sec to allow the client thread 
        to print to the console the responses from the server.

        It also execute a while loop waiting for the client thread to terminate. If you change the delay, to 7 sec for example, the message `Client thread still running` is displayed several times until the client thread terminates. 
        
        After that the function terminate the server thread shutting its forever loop, so allowing the control to go back to the `http_menu.py` module.   

        """
        server_thread = Thread(target=self.run_crud_server) 
        server_thread.start()  
        client_thread = Thread(target=self.run_crud_client)
        client_thread.start()
        
        # This delay is to allow the client thread 
        # to print to the console. 
        sleep(10)

        while client_thread.is_alive():
            # To experiment: print this in a loop by 
            # setting the sleep time to 7 seconds.
            print('Client thread still running')
        
        print('Client thread completed. Terminate the server thread also.  ')
        # Terminate the server thread. 
        self.server.shutdown()
    
