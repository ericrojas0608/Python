from selenium import webdriver

#previo a esto se debe de entrar en la web a chropath y cargar en chrome
#visualizar mediante inspeccionar si esta el componente
#en selector se debe de ingresar, ruta absolutas
# //input[@id='emailOrUsername']
driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://authn.edx.org/login")

usuario = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/input[1]")
usuario.send_keys("ericrojas0608@gmail.com")

clave = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/input[1]")
clave.send_keys("Pichos0608#")

boton = driver.find_element_by_xpath("//input[@name='sign-in']")
boton.click()

driver.quit()