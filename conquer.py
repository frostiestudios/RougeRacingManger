import socket
from appJar import gui

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.79',10000))
server_socket.listen()
client_socket, client_address = server_socket.accept()

# Create a GUI app using appjar
app = gui()

# Add a label to display messages from the server
app.addLabel("Messages")
def send_message(btn):
    message = app.getEntry("Message")
    client_socket.send(message.encode())

app.addButton("Send message", send_message)
# Run the GUI
app.go()

# Keep receiving data from the server

    # If the received data is a file
