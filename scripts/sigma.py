import pyautogui
from appJar import gui

def press_windows_button():
    pyautogui.hotkey('win')   
    pyautogui.sleep(1)
    pyautogui.typewrite('sigma simulation')
    pyautogui.press('enter')
    pyautogui.sleep(3)
    pyautogui.press('ctrl','s')

app = gui()
app.addButton("Press Windows button", press_windows_button)
app.go()
