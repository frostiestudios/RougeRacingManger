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
        link="ho"
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
def local(btn):
    if btn == ("Send Local"):
        data=app.getEntry("MessageLocal")
        with open("htdocs/messages.html", "a") as f:
            f.write(f"<section><h3>PCLOCAL</h3>")
            f.write(f"\n")
            f.write(f"<p>{data}</p></section>")
            f.write(f"\n")
def send_message(btn):
    # Get the message from the app
    message = app.getEntry("Message")
    subject = app.getEntry("Subject")
    # Send the message
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("192.168.0.121", 12345))
    s.sendall(message.encode())
def send_file(btn):
    file_path = app.getEntry("File")
    # Open the file and send it
    with open(file_path, "rb") as f:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.0.121", 12345))
        s.sendfile(f)
        s.close()

plus=u"\u2795"
minu=u"\u002D"

def settings(btn):
    if btn == "View Clients File":
        pyautogui.sleep(1)
        pyautogui.hotkey('win')

#GUI SETTINGS
app = gui("Command",useSettings=True)
app.setIcon("fav.ico")
app.startTabbedFrame("MainMenu") 

#mainmenutab
app.startTab("Main Menu")
app.setBg("red")
app.startLabelFrame("Messanger")
app.setSticky("ew")
app.addLabelEntry("Subject")
app.addLabelEntry("Message")
app.addButtons(["clear","Send"], send_message)
app.addButton("Send File", send_file)
app.addFileEntry("File")
app.stopLabelFrame()
app.addLabelEntry("Send Address")
app.stopTab()

#localcommands
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

#messanger
app.startTab("Leaderboard")
app.startLabelFrame("Send A Local Message")
app.addLabelEntry("MessageLocal")
app.addButton("Send Local", local)
app.stopLabelFrame()
app.stopTab()


app.startTab("Clients")
app.stopTab()


app.startTab("settings")
app.startLabelFrame("Client Settings")
app.addButtons(["View Clients File","Change Where Clients Are Stored"], settings)
app.stopLabelFrame()
app.startLabelFrame("About")
app.stopLabelFrame()
app.stopTab()

app.go()