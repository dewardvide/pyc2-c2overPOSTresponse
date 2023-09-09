import subprocess

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

if __name__ == "__main__":
    command_to_run = input("Enter the PowerShell command to run: ")
    run_powershell_command(command_to_run)
