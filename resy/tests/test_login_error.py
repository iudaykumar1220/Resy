import time

import pytest
from pages.register_page import SignupPage
from pages.login_page import Loginpage

@pytest.mark.usefixtures("setup_teardown")
class Test_login_Error:

    def test_only_email_entered(self):
        driver = self.driver
        logins = Loginpage(driver)
        sings=SignupPage(driver)
        sings.click_login()
        logins.login_email_input("udayjan636@gmail.com")
        logins.login_password_input("")
        logins.click_login_continue()
        alert = logins.alert_error()
        expected_message = "we couldn't validate your login information"
        assert expected_message.lower() in alert.lower(), f"Expected alert to contain '{expected_message}', but got '{alert}'"

    def test_incorrect_email_and_password(self):
        driver = self.driver
        logins = Loginpage(driver)
        sings = SignupPage(driver)
        sings.click_login()
        logins.login_email_input("udayjan636@gmail.com")
        logins.login_password_input("99999")
        logins.click_login_continue()
        email_message = logins.get_validation_message()
        assert "please" in email_message.lower() or "@" in email_message, f"Expected email validation, got: {email_message}"
        time.sleep(5)

    def test_incorrect_email_and_inncoret_password(self):
        driver = self.driver
        logins = Loginpage(driver)
        sings = SignupPage(driver)
        sings.click_login()
        logins.login_email_input("udaygmail.com")
        logins.login_password_input("99999")
        logins.click_login_continue()
        email_message = logins.get_validation_message()
        assert "please" in email_message.lower() or "@" in email_message, f"Expected email validation, got: {email_message}"
        time.sleep(5)


