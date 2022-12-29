import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_ip_address = "192.168.0.79" # Replace this with the actual IP address of the server
client_socket.connect((server_ip_address, 12345))
