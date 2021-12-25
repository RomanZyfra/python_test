from selenium import webdriver

# Указываем полный путь к geckodriver.exe на вашем ПК.
driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
driver.get("http://www.google.com")
