from selenium import webdriver
import time
import os

url = "https://google.com/search?q="
img_dir = "./dataset/"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

def get_image(query, directory):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get(url + query)
    time.sleep(10)


keyword = ['범고래']
for k in keyword:
    if not os.path.exists(img_dir + k):
        os.mkdir(img_dir + k)
    get_image(k, img_dir + k)
