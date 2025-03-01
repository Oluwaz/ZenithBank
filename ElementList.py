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

#Checking out all the elements associated with each link in the navigation bar
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[1]/a/h3')))
#try:
#    driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[1]/a/h3').click()
#except Exception as e:
#    print('The error is: ', e)

number = 1
while number < 9:
    try:
        action.move_to_element(driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li['+str(number)+']/a/h3')).perform()
        time.sleep(4)
        number += 1
    except Exception as e:
        print('The error is: ', e)


action.move_to_element(driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[1]]/a/h3')).perform()
time.sleep(8)



try:
    options = driver.find_elements(By.XPATH, '//*[@id="firstLevelList"]/li/div[1]/div/ul')
    for opt in options:
        print(opt)
except Exception as e:
    print('The error is: ', e)

#//*[@id="firstLevelList"]/li/div[2]
#//*[@id="firstLevelList"]/li/div[1]/div/ul/li[1]



#//*[@id="firstLevelList"]/li/div[1]

#action.move_to_element(driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li{number}]/a/h3')).perform()
#time.sleep(8)
#action.move_to_element(driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[2]/a/h3')).perform()
#time.sleep(8)
#action.move_to_element(driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[4]/a/h3')).perform()
#time.sleep(8)
#action.move_to_element(driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[5]/a/h3')).perform()
#time.sleep(8)
#action.move_to_element(driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[6]/a/h3')).perform()
#time.sleep(8)
#action.move_to_element(driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[7]/a/h3')).perform()
#time.sleep(8)

#wait.until(EC.element_to_be_clickable(By.XPATH, '//*[@id="header"]/div[2]/div/nav/ul/li[1]/div[1]/div/ul/li[1]/a')).click()

time.sleep(8)
#try:
 #   action.move_to_element(driver.find_element(By.XPATH, '//*[@id="Features_1"]/span[1]')).perform()
#except Exception as e:
#    print('The error is: ', e)