import pyautogui
import random
import time

time.sleep(2)
x = random.randrange(1, 6)
if x == 1:
    y = open("B1.txt", "r")
    for word in y:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
if x == 2:
    y = open("B2.txt", "r")
    for word in y:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
if x == 3:
    y = open("B3.txt", "r")
    for word in y:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
elif x == 4:
    y = open("B4.txt", "r")
    for word in y:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
if x == 5:
    y = open("B5.txt", "r")
    for word in y:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
if x == 6:
    y = open("B6.txt", "r")
    for word in y:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
