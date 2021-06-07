import pyperclip as pyperclip
from selenium import webdriver
import time
import math
import pyperclip

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id("input_value").text
    print(x)
    y = math.log(abs(12 * math.sin(int(x))))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

    alert = browser.switch_to.alert
    print(alert.text.split(':')[-1])

    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard) # записывает в буфер
finally:
    time.sleep(5)
    browser.quit()