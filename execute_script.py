from selenium import webdriver
import math
import  time
def calc(x):
    return str(math.log(abs(12 *math.sin(int(x)))))
browser = webdriver.Chrome()
link = 'http://SunInJuly.github.io/execute_script.html'
browser.get(link)
x = browser.find_element_by_id('input_value').text
new_x = calc(x)
button = browser.find_element_by_tag_name('button')
browser.execute_script("window.scrollBy(0, 100);")
input_field = browser.find_element_by_id("answer").send_keys(new_x)
checkbox = browser.find_element_by_id('robotCheckbox').click()
radiobutton = browser.find_element_by_id('robotsRule').click()
button.click()
time.sleep(5)
browser.quit()

