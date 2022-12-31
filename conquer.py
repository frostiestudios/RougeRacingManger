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
    with open("htdocs/messages.html", "a") as f:
        f.write(f"<section><h3>{addr}</h3>")
        f.write(f"\n")
        f.write(f"<p>{data}</p></section>")
        f.write(f"\n")
    # Open a message window with the received message
    app = gui("Message")
    app.infoBox("Message Received", data)
    app.playSound("tada.mp3")
    # Close the socket
    conn.close()

# Create a loop to continuously listen for incoming connections
while True:
    receive_message()

    # Open the HTML file and write the received message to it

