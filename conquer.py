import socket
from appJar import gui

def receive_message():
    # Create a socket and listen for incoming connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)

    # Accept a connection
    conn, addr = s.accept()
    print(f"Connection from {addr}")

    # Receive and decode the message
    data = conn.recv(1024).decode()
    print(f"Received: {data}")

    app = gui("Message")
    app.infoBox("Link Received", data)
    
    # Open the link
    import webbrowser
    webbrowser.open(data)

    # Close the socket
    conn.close()

while True:
    receive_message()
