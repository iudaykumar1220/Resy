import time
import pytest

from pages.registration import Signin

@pytest.mark.usefixtures("fixture_method")
class TestSignup:

    def test_signup(self):
        driver=self.driver
        reg=Signin(driver)
        # random_number = randint(1, 1000)
        # email = f"udaykumar{random_number}@gmail.com"

        reg.click_my_account()
        reg.click_register()
        reg.enter_first_name("")
        reg.enter_last_name("")
        reg.enter_email("")
        reg.enter_phone("")
        reg.enter_password("")
        reg.enter_confirm_password("")
        reg.agree_terms()
        reg.click_continue()
        all_error_texts=reg.all_errors()
        expected_failures=["Last Name must be between 1 and 32 characters!",
                            "E-Mail Address does not appear to be valid!",
                            "Telephone must be between 3 and 32 characters!",
                            "Password must be between 4 and 20 characters!"]

        for expected in expected_failures:
            assert expected in all_error_texts,f"Expected '{expected}' not found in {all_error_texts}"
        time.sleep(10)
