from  selenium import  webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 *math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    var_x = browser.find_element_by_id("input_value").text
    time.sleep(2)
    y = calc(var_x)
    time.sleep(2)
    answer = browser.find_element_by_id("answer").send_keys(y)
    time.sleep(2)
    checkbox = browser.find_element_by_id("robotCheckbox")
    print( "Value of attribute checkbox: ",  checkbox.get_attribute('required'))
    assert checkbox is not None , 'the robot is not selected by default'
    checkbox.click()

    radiobutton = browser.find_element_by_id("peopleRule")
    print("value of peopleRule is: ", radiobutton.get_attribute('checked'))
    assert radiobutton is not None, "People Rule button is not checked"

    radiobutton2 = browser.find_element_by_id("robotsRule")
    print("value of robotsRule is: ", radiobutton2.get_attribute('checked'))
    assert radiobutton2 is not None, "Robots Rule button is not checked"
    radiobutton2.click()

    button = browser.find_element_by_css_selector("button[type='Submit']")
    print("value of button before typing", button.get_attribute("disabled"))
    assert button is not None, "Button is not able"
    button.click()



    time.sleep(20)

finally:
    browser.quit()
