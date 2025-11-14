import time
import pytest

from pages.registration import Signin
from pages.login_page import LoginPage


@pytest.mark.usefixtures("fixture_method")
class TestSignup:

    def test_login_page(self):
        driver = self.driver
        reg = Signin(driver)
        log = LoginPage(driver)
        reg.click_my_account()      # Navigate to My Account
        log.open_login_page()      # Click Login
        log.enter_email("udayjan636@gmail.com")
        log.enter_password("Susmita@0305")
        log.click_login_btn()      # Click Login button
        log.account_verify()
        time.sleep(10)             # Wait for page to load
