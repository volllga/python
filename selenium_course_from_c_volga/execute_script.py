from selenium import webdriver
import time

browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing by Volga';")
browser.execute_script("document.title='Script executing by Robots';alert('Robots at work');")

browser.execute_script("window.scrollBy(0, 100);") #команда проскроллит страницу на 100 пикселей вниз
# javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView(true);

time.sleep(5)
browser.quit()


# driver = webdriver.Chrome()
# driver.get("https://SunInJuly.github.io/execute_script.html")
#
# try:
#     button = driver.find_element_by_tag_name("button")
#     _ = button.location_once_scrolled_into_view
#
#     button.click()
#     assert True
# finally:
#     time.sleep(5)
#     driver.quit()