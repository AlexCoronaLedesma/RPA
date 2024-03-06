import pyautogui
import pyperclip
import time

pyautogui.hotkey('win')
time.sleep(1)
pyautogui.typewrite('Bloc de', interval=0.1)
pyautogui.press('enter')

# Esperar unos segundos para cambiar a la ventana de la aplicación de procesamiento de texto

time.sleep(2)
# Escribir un mensaje utilizando la función typewrite()
pyautogui.typewrite('¡Hola, mundo!\n', interval=0.05)
# Presionar la tecla Enter para cambiar de línea
pyautogui.press('enter')
# Escribir otro mensaje
pyautogui.typewrite('Este es un ejemplo de PyAutoGUI.', interval=0.05)
pyautogui.press('enter')

## Modificacion ##
pyperclip.copy('Viva España')
pyautogui.hotkey('ctrl', 'v')
##################

pyautogui.hotkey('ctrl', 'g')

time.sleep(2)
pyautogui.press('enter')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')
pyautogui.press('w')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('shift')
