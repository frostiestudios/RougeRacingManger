from appJar import gui
import pyautogui
import subprocess
import os
import socket
import webbrowser

#deffinitions



app=gui("App", useSettings=True)
app.setIcon("macOS/AppIcon.appiconset/fav-1024.png")
app.startTab("Messanger")
app.stopTab()
app.go()

