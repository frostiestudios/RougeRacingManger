import socket
from appJar import gui

app = gui()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
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

# Create the GUI
app.addButtons(['Restart', 'Sleep', 'Shutdown'], [restart, sleep, shutdown])
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
