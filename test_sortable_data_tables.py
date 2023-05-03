import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By


class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_sort_last_names(self):
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/tables')
        clickable = driver.find_element(By.CSS_SELECTOR,'#table1 > thead > tr > th:nth-child(1)')
        self.driver.save_screenshot('not_sorted_last_names.png')
        ActionChains(driver)\
        .click(clickable)\
        .perform()
        self.driver.implicitly_wait(2)
        self.driver.save_screenshot('sorted_last_names.png')
        last_name_column = driver.find_elements(By.CSS_SELECTOR,'#table1 tbody tr td:nth-of-type(1)')
        last_names = [name.text for name in last_name_column]
        assert last_names == sorted(last_names)

    def test_sort_emails(self):
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/tables')
        clickable = driver.find_element(By.CSS_SELECTOR,'#table1 > thead > tr > th:nth-child(3)')
        self.driver.save_screenshot('not_sorted_emails.png')
        ActionChains(driver)\
        .click(clickable)\
        .perform()
        self.driver.implicitly_wait(2)
        self.driver.save_screenshot('sorted_emails.png')
        email_column = driver.find_elements(By.CSS_SELECTOR,'#table1 tbody tr td:nth-of-type(3)')
        emails = [email.text for email in email_column]
        assert emails == sorted(emails)

if __name__ == "__main__":
    unittest.main()