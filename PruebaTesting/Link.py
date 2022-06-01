from selenium import webdriver

#recuperar una contraseña

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://authn.edx.org/login")

link_recuperacion = driver.find_element_by_link_text("Forgot password")
link_recuperacion.click()

driver.quit()
