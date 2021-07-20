from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_xpath_form"
browser.get(link)

elements = browser.find_elements_by_tag_name("input")
for element in elements:
    element.send_keys("Hello Vasiliy")
button = browser.find_element_by_xpath("//button[text()='Submit']")
button.click()
time.sleep(10)
browser.quit()