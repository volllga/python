from selenium import webdriver
import  math
import time

link = "http://SunInJuly.github.io/execute_script.html"


browser = webdriver.Chrome()
browser.get(link)
try:
    x = browser.find_element_by_id("input_value").text
    y = math.log(abs(12 * math.sin(int(x))))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))
    browser.find_element_by_id("robotCheckbox").click()

    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element_by_class_name("btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:

    time.sleep(5)
    browser.quit()