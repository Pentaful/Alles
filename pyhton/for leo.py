import pyautogui
import time
time.sleep(2)
f = open("leotext.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(60)