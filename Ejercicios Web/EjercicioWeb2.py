from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# Inicializar el controlador de Selenium para Chrome
driver = webdriver.Chrome()
print(driver)
# Maximizar la ventana del navegador
driver.maximize_window()
# Navegar a la página de YouTube
driver.get("https://www.youtube.com/")
# Esperar unos segundos para que la página se cargue completamente
time.sleep(2)
# Encontrar y hacer clic en el botón de "Aceptar" en el mensaje de cookies (si existe)
try:
    accept_button = driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape')
    accept_button.click()
except:
    pass

# Esperar unos segundos para que la página de inicio se cargue completamente
time.sleep(10)
# Encontrar y hacer clic en la pestaña de "En directo" para ir a los vídeos destacados
videos_tab = driver.find_element(By.XPATH,'//*[@id="guide-button"]')
videos_tab.click()
# Encontrar y hacer clic en la pestaña de "En directo" para ir a los vídeos destacados
videos_tab = driver.find_element(By.XPATH,'//*[@id="items"]/ytd-guide-entry-renderer[4]')
videos_tab.click()

# Esperar unos segundos para que la página de vídeos se cargue completamente
time.sleep(10)
# Obtener los títulos de los 5 primeros vídeos destacados
featured_videos = driver.find_elements(By.XPATH,'//*[@id="video-title"]')[:5]
for index, video in enumerate(featured_videos):
    print(f"Vídeo {index + 1}: {video.text}")
# Cerrar el navegador
driver.quit()
