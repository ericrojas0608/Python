from selenium import webdriver
import time

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controlador.get("https://authn.edx.org/login")

email = controlador.find_element_by_class_name("form-control")
clave = controlador.find_element_by_class_name("form-control")

email.send_keys("ericrojas0608@gmail.com")
clave.send_keys("Pichos0608#")

boton = controlador.find_element_by_class_name("pgn__stateful-btn")
boton.click()

controlador.quit()
