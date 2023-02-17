import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = input()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.set_window_position(980, 0, windowHandle='current')
driver.get(url)
time.sleep(5)

# identify element
string = driver.find_element(By.XPATH, "//div[@class='show-info-middle-title']").text

# get_attribute() to get value of input box
print("Value of input box: " + string)
