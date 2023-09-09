import requests
import time

def send_hello_world_request():
    url = "http://192.168.1.1"  # Replace your C2 URL 
    message_body = " "   # This string will be sent to C2 to verify it's alive
    
    try:
        response = requests.post(url, data=message_body)
        if response.status_code == 200:
            print(f"Request sent successfully. Response: {response.text}")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    while True:
        send_hello_world_request()
        time.sleep(120)  # Sleep for 2 minutes (120 seconds) before sending the next request
