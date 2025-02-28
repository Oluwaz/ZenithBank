from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://zenithbankgh.euwest01.umbraco.io/")
driver.maximize_window()
print('done')

print('starting')
#Trying out the Toggle switch on the Zenith Bank website
try:
    Toggle = driver.find_element(By.XPATH, '//*[@id="themeSwitcherMobile"]/div[2]/span[2]')
    Toggle.click()
except Exception as e:
    print('The error is: ', e)


#Trying the personale in the navigation bar
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[1]/a/h3')))
    personal = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[1]/a/h3')
    personal.click()
except Exception as e:
    print('The error is: ', e)

#Trying the business in the navigation bar
print('starting 2')

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[2]/a')))
    personal = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[2]/a')
    personal.click()
except Exception as e:
    print('The error is: ', e)

    

print('ending')

