import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the IP address of the current computer
ip_address = socket.gethostbyname(socket.gethostname())
print(ip_address)
# Bind the socket to a specific IP and port
server_socket.bind((ip_address, 12345))

# Start listening for incoming connections
server_socket.listen()