import socket
from appJar import gui
import ctypes
import os

app = gui()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.0.171', 10000)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def restart(btn):
    # Restart the computer
    pass

def sleep(btn):
    # Put the computer to sleep
    pass

def shutdown(btn):
    # Shut down the computer
    pass
def select_file(btn):
    # Open a file dialog to select a file
    file_path = app.openBox()
    # Get the file name and size
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    # Update the GUI with the file name and size
    app.setLabel('File Name', file_name)
    app.setLabel('File Size', str(file_size))
    
# Create the GUI
app.addButtons(['Restart', 'Sleep', 'Shutdown'], [restart, sleep, shutdown])
app.addLabel('Select a file to send:')
app.addButton('Select File', select_file)
app.addLabel('File Name:')
app.addLabel('File Size:')
app.addLabel('Connected Clients:')
app.addLabel('IP Addresses:')
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
                if command == 'restart':
                    restart(None)
                elif command == 'sleep':
                    sleep(None)
                elif command == 'shutdown':
                    shutdown(None)
                
            else:
                print('No more data from', client_address)
                break
            
            
    finally:
        # Clean up the connection
        connection.close()
