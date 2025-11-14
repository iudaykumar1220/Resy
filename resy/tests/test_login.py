import time
import pytest
from pages.signup_page import SignupPage
from pages.login_page import Loginpage

@pytest.mark.usefixtures("setup_teardown")
class Test_login:

    def test_signup(self):
        driver = self.driver
        logins = Loginpage(driver)
        sings=SignupPage(driver)
        sings.click_login()
        logins.login_email_input("udayjan6@gmail.com")
        logins.login_password_input("Susmita@0305")
        logins.click_login_continue()
        time.sleep(10)
