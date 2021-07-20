from  selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/selects2.html"
browser.get(link)
def calc(a,b):
    return a + b


# browser.find_element_by_id('dropdown').click()
# browser.find_element_by_css_selector('option:nth-child(5)').click()
number1 = browser.find_element_by_id('num1').text
number2 = browser.find_element_by_id("num2").text
suma = calc(int(number1),int(number2))
print(suma)
time.sleep(1)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(suma))
time.sleep(2)
browser.find_element_by_css_selector("button[type='submit']").click()
time.sleep(10)
browser.quit()