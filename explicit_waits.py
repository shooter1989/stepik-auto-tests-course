from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import  math
import  time
def calc(x):
    return str(math.log(abs(12 *math.sin(int(x)))))
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

text = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
button = browser.find_element_by_id('book').click()
x = browser.find_element_by_id('input_value').text
number = calc(x)
browser.execute_script("window.scrollBy(0, 100);")
answer = browser.find_element_by_id('answer').send_keys(number)
submit_button = browser.find_element_by_id('solve').click()
time.sleep(5)
browser.quit()
