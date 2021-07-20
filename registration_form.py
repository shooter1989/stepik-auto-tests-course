from selenium import  webdriver
import  time
browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    element1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    element1.send_keys("Registration information")
    element2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    element2.send_keys("Registration information")
    element3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
    element3.send_keys("Registration information")

    button = browser.find_element_by_css_selector("button[type = 'submit']")
    button.click()
    time.sleep(10)
    welcome_text = browser.find_element_by_tag_name("h1").text


    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    browser.quit()