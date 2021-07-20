from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "https://www.foxtrot.com.ua/ru/shop/led_televizory.html"
browser.get(link)
button = browser.find_element_by_css_selector(".button[data-id='6665643']")
button.click()
time.sleep(1)
button = browser.find_element_by_css_selector(".button[data-id='6557915']")
button.click()
time.sleep(1)

browser.get("https://www.foxtrot.com.ua/ru/cart.html")
goods = browser.find_element_by_class_name("shop-cart__item-product")
assert len(goods) == 2

browser.quit()