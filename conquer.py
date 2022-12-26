import socket
from appJar import gui

app = gui()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function to handle the "Connect" button
def connect(btn):
    # Get the server IP and port from the GUI
    server_ip = app.getEntry('Server IP')
    server_port = app.getEntry('Server Port')
    try:
        # Connect the socket to the server
        server_address = (server_ip, int(server_port))
        print('Connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)
    except Exception as e:
        print('Error connecting to server:', e)

# Function to handle the "Save" button
def save(btn):
    # Get the server IP and port from the GUI
    server_ip = app.getEntry('Server IP')
    server_port = app.getEntry('Server Port')
    # Save the server IP and port to a settings file
    with open('settings.txt', 'w') as f:
        f.write(server_ip + '\n')
        f.write(server_port + '\n')

# Function to load the server IP and port from the settings file
def load_settings():
    try:
        with open('settings.txt', 'r') as f:
            server_ip = f.readline().strip()
            server_port = f.readline().strip()
            app.setEntry('Server IP', server_ip)
            app.setEntry('Server Port', server_port)
    except Exception as e:
        print('Error loading settings:', e)

# Load the server IP and port from the settings file
load_settings()

# Create the GUI
app.addLabel('Server IP:')
app.addEntry('Server IP')
app.addLabel('Server Port:')
app.addEntry('Server Port')
app.addButtons(['Connect', 'Save'], [connect, save])
app.go()

while True:
    # Wait for a connection
    print('Waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            if data:
                command = data.decode()
                # Execute the command here
                print('Received "{}"'.format(command))
            else:
                print('No more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()
