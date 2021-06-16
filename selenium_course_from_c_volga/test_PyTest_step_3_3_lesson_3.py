import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time


def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector(".first_block > .first_class > .first")
    first_name.send_keys("Michael")
    last_name = browser.find_element_by_css_selector(".first_block > .second_class > .second")
    last_name.send_keys("Jackson")
    email = browser.find_element_by_css_selector(".first_block > .third_class > .third")
    email.send_keys("michaelJ@mail.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    browser.implicitly_wait(2)
    return browser.find_element_by_tag_name("h1").text


class TestFormAutorisation(unittest.TestCase):

    def test_number_1(self):
        self.assertEqual(fill_form("http://suninjuly.github.io/registration1.html"), \
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_number_2(self):
        self.assertEqual(fill_form("http://suninjuly.github.io/registration2.html"), \
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__":
    unittest.main()

# проверка работы команды git diff