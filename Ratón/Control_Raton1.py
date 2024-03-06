import pyautogui
import time

pyautogui.moveTo(1770, 30, duration=0.1)
pyautogui.click()

# Mueve el primer archivo
pyautogui.moveTo(950, 50, duration=0.5)
pyautogui.dragTo(950, 950, button='left', duration=1)

# Mueve el segundo archivo
pyautogui.moveTo(1394, 60, duration=0.5)
pyautogui.dragTo(1400, 950, duration=1)

print(pyautogui.position())