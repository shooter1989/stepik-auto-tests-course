from selenium import  webdriver
import math
import time
import os

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)
elements = browser.find_elements_by_css_selector("input[type= 'text']")
for element in elements:
    element.send_keys("Hello world")

current_dir = os.path.abspath((os.path.dirname(__file__)))
file_name = 'hello.txt'
file_path = os.path.join(current_dir, file_name)
button = browser.find_element_by_id('file').send_keys(file_path)
submit_button = browser.find_element_by_css_selector("button[type='submit']").click()
time.sleep(10)

browser.quit()
