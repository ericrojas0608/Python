

from selenium import webdriver

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://authn.edx.org/login")

#input#emailOrUsernameinput#emailOrUsername
correo = driver.find_element_by_css_selector("input#emailOrUsername")
clave = driver.find_element_by_css_selector("input#password")

correo.send_keys("ericrojas0608@gmail.com")
clave.send_keys("Pichos0608#")

boton = driver.find_element_by_css_selector("input#sign-in")
boton.click()

driver.quit()
