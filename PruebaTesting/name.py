
from selenium import webdriver
import time

controlador = webdriver.Chrome("Drivers/chromedriver.exe")
controlador.get("https://authn.edx.org/login")

usuario = controlador.("emailOrUsername")
clave = controlador.find_element_by_name("password")

usuario.send_keys("ericrojas0608@gmail.com")
clave.send_keys("Pichos0608#")

boton = controlador.find_element_by_name("sign-in")
boton.click()

controlador.quit() #eliminar la instancia
