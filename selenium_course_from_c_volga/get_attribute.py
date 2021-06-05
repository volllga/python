from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

lnk = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(lnk)
try:
    treasure = browser.find_element_by_id("treasure")
    number = treasure.get_attribute("valuex")
    print(number)
    #number = int(number.text) #Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.
    x = calc(number)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(x)

    robot = browser.find_element_by_id("robotCheckbox")
    robot.click()

    robot_rule = browser.find_element_by_id("robotsRule")
    robot_rule.click()

    button = browser.find_element_by_class_name("btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()