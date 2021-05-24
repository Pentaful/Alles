import pyautogui
from pyautogui import *
import keyboard
import time
import win32api
import win32con

# T1 X:  614 Y:  360 RGB: ( 92,  94, 117)
# T2 X:  700 Y:  365 RGB: ( 90,  91, 117)
# T3 X:  791 Y:  368 RGB: ( 89,  91, 117)
# T4 X:  889 Y:  371 RGB: ( 90,  91, 117)
time.sleep(3)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed("q"):
    if pyautogui.pixel(614, 360)[0] == 0:
        click(614, 360)
    if pyautogui.pixel(700, 360)[0] == 0:
        click(700, 360)
    if pyautogui.pixel(791, 360)[0] == 0:
        click(791, 360)
    if pyautogui.pixel(889, 360)[0] == 0:
        click(889, 360)
