from appJar import gui
import pyautogui
import subprocess
import os
import socket
import webbrowser




def press(button):
    if button == "OpenWeb":
        webbrowser.open("http://www.google.com")
    if button == "Send Link":
        link="https://www.youtube.com/watch?v=In_PMIeHOco"
        send_message(link)
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
        pyautogui.hotkey('ctrl',"v")
    if button == "Mute":
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "toggle"])
    elif button == "Lower":
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "5%-"])
    elif button == plus:
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "5%+"])
def power(btn):
    if btn == "Restart":
        os.system("shutdown /r /t 0")
    if btn == "Shut Down":
        os.system("shutdown /s /t 1")
    if btn == "Sleep":
        subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState"])

def send_message(*message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.0.79", 12345))

    # Close the socket
    s.close()

plus=u"\u2795"
minu=u"\u002D"
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

#GUI SETTINGS
app = gui("Command",useSettings=True)
app.startTabbedFrame("MainMenu") 

app.startTab("MainMenu")  


app.startTab("Local Commands")
app.startLabelFrame("Standard Controls")
app.addButtons(["Run Sigma","Content Manager","OpenWeb","Send Link"], press)
app.stopLabelFrame()

app.startLabelFrame("Power Controls")
app.addButtons(["Restart","Shut Down","Sleep"], power)

app.stopLabelFrame()

app.startLabelFrame( "Volume Control")
app.addButtons(["Mute",minu,plus], press)
app.stopLabelFrame()

app.startLabelFrame( "Custom Commands")
app.addButtons(["C1","C2","C3","C4","C5","C6","C7","C8"], press)
app.stopLabelFrame()
app.stopTab()

app.startTab("Remote Commands")
app.addLabelTickOptionBox("clients_list",[("clients_list")])
app.startLabelFrame("Commands")
app.setLabelFont("Black")
app.stopLabelFrame()
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
app.startLabelFrame("Client Settings")
app.addButtons(["View Clients File","Change Where Clients Are Stored"], settings)
app.stopLabelFrame()
app.startLabelFrame("About")
app.start
app.stopLabelFrame()
app.stopTab()

app.go()