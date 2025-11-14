import time
from random import randint

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
        reg.enter_first_name("k uday")
        reg.enter_last_name("kumar")
        reg.enter_email("udayjan636@gmail.com")
        reg.enter_phone("7842321123")
        reg.enter_password("Susmita@0305")
        reg.enter_confirm_password("Susmita@0305")
        reg.agree_terms()
        reg.click_continue()
        time.sleep(10)
