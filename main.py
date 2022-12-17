from appJar import gui
import webbrowser
import time

# handle button events
def press(button):
    if button == "OpenWeb":
        app.open_web("http://www.google.com")

app = gui("Login Window", "400x200")
app.startTabbedFrame("MainMenu") 
app.startTab("MainMenu")  
time_label = app.addLabel("time", "")
time_label.config(font=("Arial", 20))
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    app.after(1000, update_time)
update_time() 
app.go()