from selenium import webdriver
import time

lnk = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()
browser.get(lnk)

try:
    first_name = browser.find_element_by_class_name("first")
    first_name.send_keys("Tom")

    last_name = browser.find_element_by_class_name("second")
    last_name.send_keys("Malkom")

    email = browser.find_element_by_class_name("third")
    email.send_keys("tom@gmail.com")

    browser.find_element_by_class_name("btn").click()
    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name("h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()