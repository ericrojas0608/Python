from selenium import webdriver

driver = webdriver.Chrome("Drivers/chromedriver.exe")
driver.get("https://authn.edx.org/login")
driver.maximize_window()

varios = driver.find_elements_by_class_name("form-control")
for i in varios:
    i.send_keys("Pichos0608#")
