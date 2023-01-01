from appJar import gui
import pyautogui
import subprocess
import os
import socket
import webbrowser

#socketserver
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
def main():
    client = socket.socket(socket.AF_INET, socket .SOCK_STREAM)
    client.connect(ADDR)
    file = open("data/yt.txt", "r")
    data = file.read()
    client.send("yt.text".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]:{msg}")
    file.close()
    client.close()
if __name__ == "__main__":
    main()
