from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib.request
import time
import os
import re

# https://anyflipdownload.com/njbp/ired/#pages
# https://anyflipdownload.com/njbp/ired/mobile/#pages
# https://online.anyflip.com/njbp/ired/files/mobile/1.jpg
# https://anyflip.com/njbp/ired

# https://anyflipdownload.com/nlqlf/gizt/#pages

# make download link
url = input('Anyflipdownload link: ')

before = "https://online.anyflip.com"
after = "/files/mobile/"

# pattern to extract the desired substring
pattern = r"/\w+/\w+/?"

# extract substring from URL
match = re.search(pattern, url)
substring = match.group()

# check if string ends with slash
if substring.endswith("/"):
    substring = substring.rstrip(substring[-1])
    first_page_url = before + substring + after
else:
    first_page_url = before + substring + after
print("\nLink acquired.")

# if input is anyflip.com replace with anyflipdownload.com
if 'anyflip.com' in url:
    url = url.replace("anyflip", "anyflipdownload")

# driver start
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.set_window_position(980, 0, windowHandle='current')
driver.get(url)

# find n num of pages
print("Gathering pages.")
time.sleep(5)
n = driver.find_elements(By.TAG_NAME, 'i')
n = int((len(n) - 3) / 2)

# make dir that named after date and time
path = 'D:/Minecraft Stuff/RPGs/D&D/anyflipdownload/' + driver.find_element(By.XPATH, "//div[@class='col']/h1").text
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)
print("Directory created.")

# download pages and save in folder
print("Downloading pages.")
for i in range(1, n + 1):
    page_url = first_page_url + str(i) + '.jpg'
    page_url = page_url.replace(' ', '')
    urllib.request.urlretrieve(page_url, path + '/' + str(i) + '.png')
print("Download complete.")
