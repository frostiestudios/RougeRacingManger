from appJar import gui
import webbrowser
import time
import pyautogui
import subprocess
import os

def press(button):
    if button == "OpenWeb":
        app.open_web("http://www.google.com")
    if button == "Run Sigma":
        pyautogui.hotkey('win')
        pyautogui.sleep(1)
        pyautogui.typewrite('sigma simulation')
        pyautogui.press('enter')
    if button == "New Race LB":
        pyautogui.sleep(1)
        pyautogui.typewrite('https://192.168.1.12:6001/RemoteViewSettings')
        pyautogui.press('enter')
    if button == "Mute":
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "toggle"])
    elif button == "Lower":
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "5%-"])
    elif button == "Raise":
        subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "5%+"])
def restart(btn):
    if btn == "Restart":
        os.system("shutdown /r /t 0")
    if btn == "Shut Down":
        os.system("shutdown /s /t 1")
    if btn == "Sleep":
        subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState"])
        
app = gui("RRM", "400x200")
app.startTabbedFrame("MainMenu") 
app.startTab("MainMenu")  
time_label = app.addLabel("time", "")
time_label.config(font=("Arial", 20))
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    app.after(1000, update_time)
update_time() 

app.startTab("ControlPannel")
app.button("Run Sigma", press)
app.button("New Race LB", press)
app.addButtons(["Restart","Shut Down","Sleep"], restart)
app.addLabel("l1", "Volume Control")
app.addButtons(["Mute", "Lower", "Raise"], press)
app.stopTab()


app.go()