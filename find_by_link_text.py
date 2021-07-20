import math
import time
from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_link_text"
browser.get(link)
link_text = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
link_text.click()
input = browser.find_element_by_name('first_name')
input.send_keys('Vladyslav')
time.sleep(0.5)
input2 = browser.find_element_by_name('last_name')
input2.send_keys("Shusta")
time.sleep(0.5)
input3 = browser.find_element_by_class_name('city')
input3.send_keys("Kyiv")
time.sleep(0.5)
input4 = browser.find_element_by_id('country')
input4.send_keys('Ukraine')
time.sleep(0.5)
button = browser.find_element_by_tag_name('button')
button.click()
time.sleep(10)
browser.quit()