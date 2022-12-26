import socket
from appJar import gui

# Read the server address from the configuration file
with open('config.txt') as config_file:
    server_address = config_file.readline().strip()

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_address, 8000))

# Create a GUI app using appjar
app = gui()

# Add a label to display messages from the server
app.addLabel("Messages")

# Run the GUI
app.go()

# Keep receiving data from the server
while True:
    data = client_socket.recv(1024).decode()

    # If the received data is a message, display it
    if data.startswith("message:"):
        message = data[8:]
        app.setLabel("Messages", message)

    # If the received data is a file
