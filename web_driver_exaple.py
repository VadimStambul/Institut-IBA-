from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="c:\Webdriver\chromedriver.exe")
driver.maximize_window()
driver.get('https://yandex.ru')
search = driver.find_element_by_id('text')
search.send_keys('королевская роза')
search.send_keys(Keys.ENTER)
driver.find_element_by_partial_link_text('Картинки').click()

time.sleep(3)
driver.quit()
