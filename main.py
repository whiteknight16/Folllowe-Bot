from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
USERNAME="tester_tests12"
PASSWORD="".join(os.environ["PASS"])

chrome_driver_path="C:/Development/chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.instagram.com/")
loop_condition=True
while loop_condition:
    try:
        username_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
        username_button.send_keys(USERNAME)
        loop_condition=False
    except TimeoutException:
        pass

loop_condition=True
while loop_condition:
    try:
        password_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
        password_button.send_keys(PASSWORD)
        password_button.send_keys(Keys.ENTER)
        loop_condition=False
    except TimeoutException:
        pass



driver.get("https://www.instagram.com/python.hub/")
time.sleep(3)

followers_button=driver.find_element(By.XPATH,'//*[@id="mount_0_0_Ik"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
followers_button.click()

while True:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', followers_button)
    time.sleep(1)
