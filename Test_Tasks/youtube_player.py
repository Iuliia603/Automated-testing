from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера браузера
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=5R_3iuNNUk0&t=1s")

# Подождите, чтобы убедиться, что плеер загрузился (возможно, вам потребуется изменить время ожидания)
time.sleep(30)

# Найдите элемент плеера по классу
player = driver.find_element(By.CLASS_NAME, "html5-video-player")
fullscreen_button = player.find_element(By.CLASS_NAME, '"ytp-miniplayer-button")')


# Теперь вы можете выполнять действия с найденным элементом, например, кликнуть на него
fullscreen_button.click()


