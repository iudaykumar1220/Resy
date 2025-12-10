import time
import pytest

from pages.registration import Signin
from pages.login_page import LoginPage


@pytest.mark.usefixtures("fixture_method")
class Test_Login_page_error:

    def test_invalid_emai_password(self):
        driver=self.driver
        reg=Signin(driver)
        log=LoginPage(driver)
        reg.click_my_account()
        log.click_login()
        log.enter_email("")
        log.enter_password("")
        log.click_login_btn()
        log.account_verify()
        time.sleep(10)




