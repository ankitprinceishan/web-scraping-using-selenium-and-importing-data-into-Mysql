from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=23EBNC0VOWKRV&sprefix=laptop%2Caps%2C552&ref=nb_sb_noss_2")

elem = driver.find_element(By.CLASS_NAME, "puis-card-container")

print (elem)


time.sleep(20)
driver.close()
