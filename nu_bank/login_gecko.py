import os
import random
import string
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

firefox_options = FirefoxOptions()

# Add the argument and make the browser Headless.
firefox_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")

driver = webdriver.Firefox(executable_path = "./geckodriver.exe", options = firefox_options)
driver.get('https://app.nubank.com.br/#/login')

# Me doy cuenta que la pagina carga el formulario dinamicamente luego de que la carga incial ha sido completada
# Por eso tengo que esperar que aparezca
input_user = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))

# Obtengo los inputs de usuario (linea 28) y password
input_pass = driver.find_element(By.XPATH, '//*[@id="input_001"]')

# Escribo mi usuario input
input_user.send_keys("1007509653")

# Escribo mi contrasena en el input
input_pass.send_keys("password123")
sleep(10)

# Obtengo el boton de login
login_button = driver.find_element(By.XPATH, '/html/body/navigation-base/div[1]/div/main/div[1]/div/div[1]/form/button')

# Le doy click
login_button.click()
