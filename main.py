from appJar import gui
import webbrowser
import time
import pyautogui

def press(button):
    if button == "OpenWeb":
        app.open_web("http://www.google.com")
    if button == "Run Sigma":
        pyautogui.hotkey('win')
        pyautogui.sleep(1)
        pyautogui.typewrite('sigma simulation')
        pyautogui.press('enter')
    if button == "New Race LB":
        pyautogui.hotkey('win')
        pyautogui.sleep(1)
        pyautogui.typewrite('https://192.168.1.12:6001/RemoteViewSettings')
        pyautogui.press('enter')
    if button == "Content Manager":
        pyautogui.hotkey('win')
        pyautogui.sleep(2)
        pyautogui.typewrite('content manager')
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.press('control'+'v')

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
app.button("Content Manager", press)
app.stopTab()


app.go()