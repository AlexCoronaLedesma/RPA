import pyautogui
import time
time.sleep(5)
# Capturar una captura de pantalla
captura = pyautogui.screenshot()
# Guardar la captura de pantalla como un archivo de imagen temporal
captura_path = "captura_temporal.png"
captura.save(captura_path)
x, y = pyautogui.locateCenterOnScreen('MicrosoftEdge.png',confidence=0.9)
pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
pyautogui.click(x, y,clicks=2,interval=0.2)
time.sleep(2)
pyautogui.alert("Imagen encontrada y clic realizando en el centro.")