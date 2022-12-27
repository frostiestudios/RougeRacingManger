from appJar import gui
import webbrowser
import time
import pyautogui
import subprocess
import os
import io


def press(button):
    if button == "OpenWeb":
        app.open_web("http://www.google.com")
    if button == "Run Sigma":
        pyautogui.hotkey('win')
        pyautogui.sleep(1)
        pyautogui.typewrite('sigma simulation')
        pyautogui.press('enter')
    if button == "Content Manager":
        pyautogui.sleep(1)
        pyautogui.hotkey('win')
        pyautogui.sleep(3)
        pyautogui.typewrite('content manager')
        pyautogui.sleep(2)
        pyautogui.press('enter')
    if button == "Mute":
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "toggle"])
    elif button == "Lower":
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "5%-"])
    elif button == "Raise":
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "5%+"])
def power(btn):
    if btn == "Restart":
        os.system("shutdown /r /t 0")
    if btn == "Shut Down":
        os.system("shutdown /s /t 1")
    if btn == "Sleep":
        subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState"])
        
def client(btn):
    if btn == "ADD":
        cnm = app.getEntry("Client Name")
        cip = app.getEntry("IP")
        with open ( "clients.cfg","a") as outFile:
            outFile.write("client name: ")
            outFile.write(cnm)
            outFile.write("\n")
            outFile.write("ip adress  : ")
            outFile.write(cip)
            outFile.write("\n")
            outFile.write("------ \n")
            outFile.close()
        print(cnm,cip)
        
        
def settings(btn):
    if btn == "View Clients File":
        pyautogui.sleep(1)
        pyautogui.hotkey('win')


app = gui("Command")
app.startTabbedFrame("MainMenu") 

app.startTab("MainMenu")  


app.startTab("Local Commands")
app.addLabel("l1","Standard Controls")
app.addButtons(["Run Sigma","Content Manager"], press)
app.addLabel("l2","Power Controls")
app.addButtons(["Restart","Shut Down","Sleep"], power)
app.addLabel("l3", "Volume Control")
app.addButtons(["Mute", "Lower", "Raise"], press)
app.stopTab()

app.startTab("Clients")
app.addListBox("clients_list")
with open("clients.cfg") as clients_file:
    for line in clients_file.readlines():
        if line.startswith("Client Name:"):
            client_name = line[12:].strip()
            app.addListItem("clients_list", client_name)
app.addButton("Add New", client)
app.stopTab()

app.startTab("New Client")
app.addLabelEntry("Client Name")
app.addLabelEntry("IP")
app.addButtons(["Clear","ADD"],client)
app.stopTab()

app.startTab("settings")
app.startFrame("Client Settings")
app.addButtons(["View Clients File"], settings)
app.stopFrame()
app.stopTab()

app.go()