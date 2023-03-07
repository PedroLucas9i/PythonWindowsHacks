import pyautogui
import ctypes
ctypes.windll.kernel32.FreeConsole()
pyautogui.hotkey('win', 'r')
pyautogui.typewrite("cmd")
pyautogui.hotkey('enter')
pyautogui.moveTo(200, 500)
pyautogui.press('f11')
pyautogui.click()
pyautogui.hotkey('enter')
pyautogui.typewrite("color a")
pyautogui.hotkey('enter')
pyautogui.typewrite("dir/s")
pyautogui.hotkey('enter')
