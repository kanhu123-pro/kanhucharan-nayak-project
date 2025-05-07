from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get(r"https://www.facebook.com/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'div[id="email_container"]>input[type="text"]').send_keys("qwerty")
driver.find_element(By.CSS_SELECTOR,'div[class="_55r1 _1kbt"]>[type="password"]').send_keys("12344")
driver.find_element(By.CSS_SELECTOR,'div[class="_xkt"]>button[class="_42ft _4jy0 _52e0 _4jy6 _4jy1 selected _51sy"').click()
time.sleep(3)