import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import pickle

vk_phone = "+375293728338"
vk_password = "3728338Python"

class Vk(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="c:\Webdriver\chromedriver.exe")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        self.driver.get("https://vk.com/")
        self.assertIn('Welcome! | VK', driver.title)
        print("Passing authentication...")
        email_input = self.driver.find_element_by_id("index_email")
        email_input.clear()
        email_input.send_keys(vk_phone)
        time.sleep(5)
        password_input = self.driver.find_element_by_id("index_pass")
        password_input.clear()
        password_input.send_keys(vk_password)
        time.sleep(3)
        password_input.send_keys(Keys.ENTER)
        self.driver.find_element_by_id("index_login_button").click()
        time.sleep(7)

        print("Going to the profile page...")
        profile_page = self.driver.find_element_by_id("l_pr").click()
        time.sleep(5)

        print("Click on the comment icon...")
        comment_icon = self.driver.find_element_by_class_name("_comment").find_element_by_class_name(
            "like_button_icon").click()
        time.sleep(5)

        print("Writing a comment...")
        self.driver.find_elements_by_class_name("submit_post_field")[1].send_keys("Hey! I was here!" + Keys.ENTER)
        time.sleep(5)
        print("The work is done!")


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

