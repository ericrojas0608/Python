#Llamar el modulo selenium e importar el webdriver
from selenium import webdriver

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F%3Futm_source%3DGoogle")
driver.close() #Permite cerrar la instancia
