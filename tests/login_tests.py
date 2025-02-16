from tests.base_test import BaseTest

from time import sleep

class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Dodatkowy warunek wstępny - wejście na stronę logowania
        self.login_page = self.home_page.click_log_in()

    def testEmptyLogin(self):
        # (nie wpisujemy nic)
        # 1. Kliknij LogIn
        self.login_page.click_log_in()
        # Sprawdź, czy wyświetla się alert "Please fill out Username and Password."
        self.assertEqual("Please fill out Username and Password.", self.login_page.get_alert_message())
        self.login_page.confirm_alert()

    def testValidLogin(self):
        username = "tester_alk"
        # 1. Wpisz login
        self.login_page.enter_username(username)
        # 2. Wpisz haslo
        self.login_page.enter_password("haslo")
        # 3. Kliknij Log In
        self.login_page.click_log_in()
        # 4. Sprawdź, czy w prawym górnym rogu widnieje powitanie "Welcome tester_alk"
        welcome_text_act = self.home_page.get_welcome_username_text()
        self.assertEqual(f"Welcome {username}", welcome_text_act)
        # 5. (Sprawdź, czy można kliknąć LogOut)
        # TODO:
        sleep(1.5)