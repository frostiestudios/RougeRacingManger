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
<<<<<<< Updated upstream

    # Open a message window with the received message
    app = gui("Message")
    app.infoBox("Message Received", data)

=======
    with open ( "messages.html","a") as outFile:
        outFile.write(addr)
        outFile.write(data)
        outFile.close()
    # Open a message window with the received message
    app=gui("Messanger")
    app.infoBox("Message Received", data)
>>>>>>> Stashed changes
    # Close the socket
    conn.close()
while True:
    receive_message()

