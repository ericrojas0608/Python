from selenium import webdriver

#previo a esto se debe de entrar en la web a chropath y cargar en chrome
#visualizar mediante inspeccionar si esta el componente
#en selector se debe de ingresar, ruta relativa //input[@id='emailOrUsername']
driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://authn.edx.org/login")

usuario = driver.find_element_by_xpath("//input[@id='emailOrUsername']")
usuario.send_keys("ericrojas0608@gmail.com")

clave = driver.find_elem#ent_by_xpath("//input[@name='password']")
clave.send_keys("Pichos0608#")

boton = driver.find_element_by_xpath("//input[@name='sign-in']")
boton.click()

driver.quit()