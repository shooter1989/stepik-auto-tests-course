from selenium import  webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 *math.sin(int(x)))))
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

button = browser.find_element_by_css_selector('button[type="submit"]').click()
confirm = browser.switch_to_alert()
confirm.accept()
x = browser.find_element_by_id('input_value').text
result = calc(x)
answer = browser.find_element_by_id('answer').send_keys(result)
submit = browser.find_element_by_css_selector("button[type='submit']").click()