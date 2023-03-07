import pyautogui
import time
from ctypes import WinDLL
user32 = WinDLL("user32")
pyautogui.hotkey('win', 's')
time.sleep(0.2)
pyautogui.typewrite("youtube.com")
time.sleep(0.2)
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.leftClick(637, 600)
for _ in range(50):
    user32.keybd_event(0xAF, 0, 0, 0)
    user32.keybd_event(0xAF, 0, 2, 0)