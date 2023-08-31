
import requests

# Server URL
url = "http://139.59.28.124:5000/api/messages"

# Sending a message to the server
data = {"message": "Hello server"}
response = requests.post(url, json=data)
print("Server Response:", response.text)

# Receiving messages from the server
response = requests.get(url)
if response.status_code == 200:
    received_data = response.json()
    server_message = received_data.get('message', '')
    print("Received message from server:", server_message)
else:
    print("Failed to receive message from server.")