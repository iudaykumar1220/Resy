import time

import pytest
from pages.signup_page import SignupPage
from pages.login_page import Loginpage

@pytest.mark.usefixtures("setup_teardown")
class Test_login_Error:

    # def test_only_email_entered(self):
    #     driver = self.driver
    #     logins = Loginpage(driver)
    #     sings=SignupPage(driver)
    #     sings.click_login()
    #     logins.login_email_input("udayj.com")
    #     logins.login_password_input("")
    #     logins.click_login_continue()
    #     alert = logins.alert_error()
    #     expected_message = "we couldn't validate your login information"
    #     assert expected_message.lower() in alert.lower(), f"Expected alert to contain '{expected_message}', but got '{alert}'"

    def test_incorrect_email_and_password(self):
        driver = self.driver
        logins = Loginpage(driver)
        sings = SignupPage(driver)
        sings.click_login()
        logins.login_email_input("uday")
        logins.login_password_input("")
        logins.click_login_continue()
        # logins.alert_error()
        email_message = logins.get_validation_message(logins.login_email)
        assert "please" in email_message.lower() or "@" in email_message, f"Expected email validation, got: {email_message}"


        # password_message = logins.get_validation_message(logins.login_password)
        # assert "Please" in email_message.lower()
        # assert "" in password_message.lower() or "required" in password_message.lower()



