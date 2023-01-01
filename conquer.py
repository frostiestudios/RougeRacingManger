import socket
from appJar import gui

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
def main():
    print("[starting]server is starting")
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """ Starting a TCP socket"""
    server.bind(ADDR)
    """ Bind the IP and PORT to the server. """
    server.listen()
    """ Server is listening, i.e., server is now waiting for the client to connected. """
    print("[LISTENING] Server Is Listening")
    while True:
        conn, addr = server.accept()
        print(f"[NEW CON]{addr} connected to the server")
        #filename
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))
        #filedata
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))
        #closefile
        file.close()
        conn.close()
        print(f"[DISCONNECTED]{addr}DISCONNECTED")
if __name__ == "__main__":
    main()