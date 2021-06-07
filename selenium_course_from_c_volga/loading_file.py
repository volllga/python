import os #OS module in Python provides various methods for interacting with the operating system
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
file_name = "file.txt" # имя файла, который будем загружать на сайт
current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого скрипта loading_file.py
                                                        # os.path is a submodule of OS module which contains some useful functions on pathnames
file_path = os.path.join(current_dir, file_name) # получаем путь к file_example.txt

try:
    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.send_keys("Jon")

    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.send_keys("Anderson")

    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys("anderson@gmail.com")

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path) # отправляем файл

    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
