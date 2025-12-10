import time
import pytest
# from random import randint
from pages.register_page import SignupPage

@pytest.mark.usefixtures("setup_teardown")
class TestRegister:

    # def random_email(self):
    #     return f"uday{randint(0, 1000)}kumar@gmail.com"

    def test_register(self):

        signup = SignupPage(self.driver)

        signup.click_login()
        signup.click_signup()
        signup.enter_phone("8688264205")
        signup.wait_until_captcha_solved()
        signup.click_continue()
        signup.enter_otp_manually()
        # signup.click_create_account()
        signup.enter_first_name("susmita")
        signup.enter_last_name("uday")
        signup.enter_email("pravinuday0@gmail.com")
        signup.click_marketing_checkbox()
        signup.click_terms_checkbox()
        # signup.wait_until_recaptcha_solved()
        signup.click_submit()
        time.sleep(5)




