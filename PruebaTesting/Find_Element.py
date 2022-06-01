from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://authn.edx.org/login")
driver.maximize_window()

correo = driver.find_element(By.ID, "emailOrUsername")
correo.send_keys("ericrojas0608@gmail.com")

clave = driver.find_element(By.ID, "password")
clave.send_keys("Pichos0608#")

boton = driver.find_element(By.ID, "sign-in")
boton.click()

driver.quit()

