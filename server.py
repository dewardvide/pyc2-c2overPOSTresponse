import http.server
import socketserver
#import urllib.parse


# Define the server's listening address and port
host = "localhost"
port = 8080

# Define a custom request handler to handle incoming requests
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        #THIS IS HERE FOR TESTING PURPOSES
        # Define the response string which is the command you would like to run perhaps we should change this to input
        response = "Hello World!"

        # Set the response headers
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", len(response))
        self.end_headers()

        # Send the response
        self.wfile.write(response.encode("utf-8"))

    def do_POST(self):

        # Get the length of the request body
        content_length = int(self.headers['Content-Length'])

         # Read the request body data as bytes
        post_data = self.rfile.read(content_length)

        # Decode the bytes as a UTF-8 string
        message_body = post_data.decode('utf-8')
        
        # Append the message body to a text file
        with open('received_messages.txt', 'a') as file:
            file.write(message_body + '\n')

        response_string = "whoami"

        # Set the response headers
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", len(response_string))
        self.end_headers()

        #send response string 
        self.wfile.write(response_string.encode('utf-8'))
        
# Create an HTTP server with the custom request handler
with socketserver.TCPServer((host, port), MyHandler) as httpd:
    print(f"Server started at http://{host}:{port}")
    httpd.serve_forever()