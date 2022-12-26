import socket
from appJar import gui

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a host and port
server_socket.bind(('localhost', 8000))

# Start listening for incoming connections
server_socket.listen()

# Accept an incoming connection
client_socket, client_address = server_socket.accept()

# Create a GUI app using appjar
app = gui()

# Add a button to send a message to the client
def send_message(btn):
    message = app.getEntry("Message")
    client_socket.send(message.encode())

app.addButton("Send message", send_message)

# Add a button to send a file to the client
def send_file(btn):
    file_path = app.openBox()
    with open(file_path, 'rb') as file:
        client_socket.sendall(file)

app.addButton("Send file", send_file)

# Add a button to send a sleep command to the client
def send_sleep_command(btn):
    client_socket.send("sleep".encode())

app.addButton("Send sleep command", send_sleep_command)

# Add a button to send a reset command to the client
def send_reset_command(btn):
    client_socket.send("reset".encode())

app.addButton("Send reset command", send_reset_command)

# Run the GUI
app.go()
