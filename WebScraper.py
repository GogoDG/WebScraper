from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib.request
import time
import os
import re

# make download link
url = input('Anyflipdownload link: ')

before = "https://online.anyflip.com"
after = "/files/mobile/"

# extract substring from URL
pattern = r"/\w+/\w+/?"
match = re.search(pattern, url)
substring = match.group()

# check if string ends with slash
if substring.endswith("/"):
    substring = substring.rstrip(substring[-1])

first_page_url = before + substring + after
print("\nLink acquired.")

# if input is anyflip.com replace with anyflipdownload.com
if 'anyflipdownload.com' in url:
    url = url.replace("anyflipdownload", "anyflip")

# driver start
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.set_window_position(980, 0, windowHandle='current')
driver.get(url)

# find n num of pages
print("Gathering pages.")
time.sleep(5)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='show-iFrame-book']"))
n = driver.find_elements(By.XPATH, "//p[@class='title']")
n = len(n)
driver.switch_to.default_content()

# make dir that named after page name
folder_name = driver.find_element(By.XPATH, "//div/a/div/span[@title]").text
path = 'D:/Minecraft Stuff/RPGs/D&D/anyflipdownload/' + folder_name
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

# take images and convert them to pdf
images = [i for i in os.listdir(path) if i.endswith('png')]
images.sort(key=lambda test_string: list(map(int, re.findall(r'\d+', test_string)))[0])
converted_images = []
for image in images:
    img = Image.open(path + "/" + image)
    converted_image = img.convert('RGB')
    converted_images.append(converted_image)
image_1 = converted_images[0]
converted_images.pop(0)
image_1.save(path + "/" + folder_name + ".pdf", save_all=True, append_images=converted_images)
print("PDF created.")
