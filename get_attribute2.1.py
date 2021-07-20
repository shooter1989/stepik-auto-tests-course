from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12 *math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'
browser.get(link)
try:
    image_valuex = browser.find_element_by_id("treasure").get_attribute("valuex")
    y = calc(image_valuex)
    answer = browser.find_element_by_id("answer").send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_id("robotsRule").click()
    submit = browser.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(15)
finally:
    browser.quit()
