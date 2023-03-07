import pyautogui
import time
frase = "Seu PC vai dormir em 3.........2..........1........0...bye"
contador = 0
contador2 = 0
pyautogui.hotkey('win', 's')
time.sleep(0.1)
pyautogui.typewrite("notepad")
time.sleep(0.2)
pyautogui.hotkey('enter')
time.sleep(0.5)
while (contador != len(frase)):
    pyautogui.typewrite(frase[contador])
    contador += 1
pyautogui.hotkey('alt', 'f4')
pyautogui.hotkey('enter')
time.sleep(0.2)
pyautogui.typewrite("bye")
pyautogui.hotkey('enter')
time.sleep(0.2)
while contador2 != 7:
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('enter')
    pyautogui.leftClick(637, 600)