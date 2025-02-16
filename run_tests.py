import os
import unittest
from tests.login_tests import LoginTest

# Ładujemy testy, z TestCase
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Lista testów do uruchomienia
tests_for_run = [
    login_tests,
    # ...
    # ...
]

# Łączymy testy w Test Suitę
test_suite = unittest.TestSuite(tests_for_run)

# Odpal testy
unittest.TextTestRunner().run(test_suite)

