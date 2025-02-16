from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePageLocators:
    """
    Home Page locators
    """
    LOG_IN_A = (By.ID, "login2")
    NAME_OF_USER_A = (By.ID, "nameofuser")

class HomePage(BasePage):
    """
    Home Page object
    """
    def click_log_in(self):
        """
        Clicks log in link
        :return: LoginPage instance
        """
        # 1. Znajdź przycisk log in
        # 2. Kliknij w niego
        self.driver.find_element(*HomePageLocators.LOG_IN_A).click()
        # Zwróć stronę logowania
        return LoginPage(self.driver)

    def get_welcome_username_text(self):
        """
        Gets Welcome <USERNAME> message from the top right of the page
        :return: Welcome <USERNAME> text
        """
        # Czekamy na Welcome <USERNAME>
        self.wait_5s.until(EC.text_to_be_present_in_element(HomePageLocators.NAME_OF_USER_A, "Welcome"))
        return self.driver.find_element(*HomePageLocators.NAME_OF_USER_A).text

    def click_contact(self):
        """
        Clicks contact
        :return:
        """
        # TODO:
        pass

    def _verify_page(self):
        # TODO:
        print("Weryfikacja strony głównej")
        assert self.driver.title == "STORE"
        # ... TODO: Więcej...