from selenium import webdriver

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://authn.edx.org/login")

correo = driver.find_element_by_css_selector("input.form-control")
clave = driver.find_element_by_css_selector("input.form-control")

correo.send_keys("ericrojas0608@gmail.com")
clave.send_keys("Pichos0608#")

boton = driver.find_element_by_css_selector("input.login-button-width")
boton.click()

driver.quit()