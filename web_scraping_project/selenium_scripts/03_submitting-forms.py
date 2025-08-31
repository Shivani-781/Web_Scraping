import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://github.com/login'
driver.get(url)
time.sleep(2)

# username field
username_field = driver.find_element(By.ID, 'login_field')
username_field.send_keys('shivani')
time.sleep(1)

# password field
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('pass123')
time.sleep(1)

# submit button
submit_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[2]/form/div[3]/input')
submit_button.click()
time.sleep(2)

driver.quit()
