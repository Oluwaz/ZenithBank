from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://zenithbankgh.euwest01.umbraco.io/")
action = ActionChains(driver)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
print('done')


Personal = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[1]/a/h3')

action.move_to_element(Personal).perform()
driver.find_element(By.XPATH, '//*[@id="firstLevelList"]/li/div[1]/div/ul/li[1]/a').click()

Feature = driver.find_element(By.XPATH, '//*[@id="section_49b3d5db-1193-476d-8c51-876e4dca82db"]/div/div[2]/div[4]/div[1]')
Request = driver.find_element(By.XPATH, '//*[@id="section_49b3d5db-1193-476d-8c51-876e4dca82db"]/div/div[2]/div[4]/div[2]')
Benefit = driver.find_element(By.XPATH, '//*[@id="section_49b3d5db-1193-476d-8c51-876e4dca82db"]/div/div[2]/div[4]/div[3]')


try:
    action.scroll_to_element(Feature).perform()
    Feature.click()
except Exception as e:
    print('The error is: ', e)
time.sleep(5)
try:
    action.scroll_to_element(Request).perform()
    Request.click()
except Exception as e:
    print('The error is: ', e)
time.sleep(5)
try:
    action.scroll_to_element(Benefit).perform()
    Benefit.click()
except Exception as e:
    print('The error is: ', e)


time.sleep(5)
