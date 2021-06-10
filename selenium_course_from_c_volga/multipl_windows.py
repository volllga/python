from selenium import webdriver
import time
import math
import pyperclip

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    container = browser.find_element_by_class_name("btn")
    container.click()
    window = browser.window_handles
    print(window)

    browser.switch_to.window(window[1])

    x = browser.find_element_by_id("input_value").text
    y = math.log(abs(12 * math.sin(int(x))))
    print(x)
    print(y)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    button = browser.find_element_by_class_name("btn")
    button.click()

    alert = browser.switch_to.alert
    number = alert.text.split(":")[-1]
    print(number)
    pyperclip.copy(number)  # записывает в буфер
    alert.accept()


finally:
    time.sleep(3)
    browser.quit()
