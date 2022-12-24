import pyautogui
from appJar import gui


pyautogui.hotkey('win')   
pyautogui.sleep(1)
pyautogui.typewrite('sigma simulation')
pyautogui.press('enter')
pyautogui.sleep(3)
pyautogui.press('ctrl','s')

app = gui()
app.addLabel("Sigma Now Running")
app.go()
