import unittest
from selenium import webdriver
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        service = webdriver.ChromeService(executable_path="/usr/local/bin/chromedriver") # Mac
        self.driver = webdriver.Chrome(service=service) # Mac
        # self.driver = webdriver.Chrome() # reszta
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()