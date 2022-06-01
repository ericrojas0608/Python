#selenium es la api
from selenium import webdriver
import time

#variable que contenfa las intrucciones que se van a ejecutar
controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

#Get Permite tomar el link a testear
controlador.get("https://authn.edx.org/login")

#cuando se instancia al atributo id
'''
usuario = controlador.find_element_by_id("emailOrUsername")
usuario.send_keys("ericrojas0608@gmail.com")
time.sleep(1)

clave = controlador.find_element_by_id("password")
clave.send_keys("Pichos0608#")
time.sleep(1)

boton = controlador.find_element_by_id("sign-in")
boton.click()
time.sleep(1)

controlador.quit()
'''
#cuando se instancia al atributo name