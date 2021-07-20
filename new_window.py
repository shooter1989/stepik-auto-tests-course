from selenium import  webdriver
import time
import math
import  os
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)
button = browser.find_element_by_css_selector('button[type="submit"]').click()
new_window = browser.window_handles[1]
browser.switch_to_window(new_window)
x = browser.find_element_by_id('input_value').text
value_x = calc(x)
input = browser.find_element_by_id('answer').send_keys(value_x)
submit = browser.find_element_by_css_selector("button[type='submit']").click()
time.sleep(10)

browser.quit()