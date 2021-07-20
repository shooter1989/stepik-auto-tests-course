import time
from selenium.webdriver.common.by import By
from selenium import webdriver

link = "https://www.sb.starnavi.io"
#try:
browser = webdriver.Chrome()
browser.get(link)
button_seo = browser.find_element_by_css_selector("header [role="button"]")
button_seo.click()
meta_title = browser.find_element_by_id("metaTitle")
meta_title.send_keys("My title")
publish_button = browser.find_element_by_css_selector("header button:nth-child(3)")
#publish_button.click()
time.sleep(10)

#finally:
    #browser.quit()
