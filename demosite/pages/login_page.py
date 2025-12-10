from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators
        self.log_login = (By.XPATH, "//a[normalize-space()='Login']")
        self.log_email = (By.XPATH, "//input[@id='input-email']")
        self.log_password = (By.XPATH, "//input[@id='input-password']")
        self.log_btn = (By.XPATH, "//input[@value='Login']")
        self.verify=(By.XPATH,"//h2[normalize-space()='My Orders']")

    def click_login(self):
        """Click only on the 'Login'"""
        login_btn = self.wait.until(EC.element_to_be_clickable(self.log_login))
        login_btn.click()

    def enter_email(self, email):
        """Enter the email address."""
        email_field = self.wait.until(EC.presence_of_element_located(self.log_email))
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        """Enter the password."""
        password_field = self.wait.until(EC.presence_of_element_located(self.log_password))
        password_field.clear()
        password_field.send_keys(password)

    def click_login_btn(self):
        button = self.wait.until(EC.element_to_be_clickable(self.log_btn))
        button.click()

    def account_verify(self):
        my_orders = self.wait.until(EC.visibility_of_element_located(self.verify))
        assert "My Orders" in my_orders.text, f"Login failed {my_orders.text}"




