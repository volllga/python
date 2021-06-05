from selenium import webdriver
import  math
import time

link = "http://SunInJuly.github.io/execute_script.html"


browser = webdriver.Chrome()
browser.get(link)
try:
    x = browser.find_element_by_id("input_value").text
    y = math.log(abs(12 * math.sin(int(x))))

    footer = browser.find_element_by_class_name("bg-light")
    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))
    browser.find_element_by_id("robotCheckbox").click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:

    time.sleep(5)
    browser.quit()