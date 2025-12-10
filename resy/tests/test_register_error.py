import time
import pytest
from pages.register_page import SignupPage

@pytest.mark.usefixtures("setup_teardown")
class TestErrorRegister:

    def test_error_register(self):
        driver=self.driver
        signup=SignupPage(driver)
        signup.click_login()
        signup.click_signup()
        signup.enter_phone("8688264205")
        signup.wait_until_captcha_solved()
        signup.click_continue()
        signup.enter_otp_manually()
        signup.enter_first_name("")
        signup.enter_last_name("")
        signup.enter_email("")
        signup.click_marketing_checkbox()
        signup.click_terms_checkbox()
        signup.wait_until_recaptcha_solved()
        signup.click_submit()
        errors=signup.get_error_messages()
        assert any("required" in e.lower() for e in errors), "Required field error not displayed"
        print("Validation errors displayed correctly:", errors)
        time.sleep(5)



