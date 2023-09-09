# pyc2-c2overPOSTresponse

This project is still under development. This is a simmple C2 server that allows you to run Powershell commands. 
I am still a n33b at this but I believe that I will get better through help and suggestions from the community : ) 

## Installation

Download the .py files and run them. 

## Usage

For now you can only ran a command at a time. Open server.py and enter the command you want to be in the http response as shown below

``` 
        response_string = "whoami"

        # Set the response headers
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", len(response_string))
        self.end_headers()

        #send response string 
        self.wfile.write(response_string.encode('utf-8'))
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)