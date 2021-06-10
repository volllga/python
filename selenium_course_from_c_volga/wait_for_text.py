from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

try:
    button = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100") #.text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")
    )
    button.click()

    x = browser.find_element_by_id("input_value").text
    y = math.log(abs(12 * math.sin(int(x))))
    print(x, y)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    solve = browser.find_element_by_id("solve")
    solve.click()

    alert = browser.switch_to.alert
    number = alert.text.split(":")[-1]
    print(number)
    alert.accept()

finally:
    browser.quit()