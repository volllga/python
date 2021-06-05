from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element_by_id("num1").text
    print(num1)
    num2 = browser.find_element_by_id("num2").text
    print(num2)
    sum = int(num1) + int(num2)
    print(sum)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum))

    browser.find_element_by_class_name("btn").click()
finally:
    time.sleep(5)
    browser.quit()