import socket
from appJar import gui


# Create a GUI app using appjar
app = gui()


# Add a label to display messages from the server
app.addLabel("Conqueror")
app.addLabelAutoEntry("Enter Server IP",words=["Enty"])

# Run the GUI
app.go()

# Keep receiving data from the server

    # If the received data is a file
