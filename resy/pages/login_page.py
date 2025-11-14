
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class Loginpage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # locators for login
        self.login_email = (By.XPATH, "//input[@id='email']")
        self.login_password = (By.XPATH, "//input[@id='password']")
        self.login_continue = (By.XPATH, "//button[@class='Button Button--primary Button--lg']")
        self.alerts=(By.XPATH,"//div[@role='alert']")


    def login_email_input(self,email):
        input_email=self.wait.until(EC.presence_of_element_located(self.login_email))
        input_email.send_keys(email)

    def login_password_input(self,password):
        input_password=self.wait.until(EC.presence_of_element_located(self.login_password))
        input_password.send_keys(password)

    def click_login_continue(self):
        button = self.wait.until(EC.presence_of_element_located(self.login_continue))
        button.click()

    def alert_error(self):
        try:
            alert_elem = self.wait.until(EC.visibility_of_element_located(self.alerts))
            alert_text = alert_elem.text
            print("Alert Message:", alert_text)
            return alert_text
        except:
            print("Alert did not appear on the page.")
            return ""


    def get_validation_message(self, field):
        element = self.wait.until(EC.presence_of_element_located(field))
        message = self.driver.execute_script("return arguments[0].validationMessage;", element)
        print("Validation Message:", message)
        return message



    # def errors_msg_display(self,mails):
    #     email_input = self.wait.until(EC.presence_of_element_located(self.login_email))
    #     email_input.send_keys(mails)  # invalid email
    #     email_input.submit()  # or click Continue button if needed
    #
    #     # Capture the built-in browser validation message
    #     message = self.driver.execute_script("return arguments[0].validationMessage;", email_input)
    #     print("Validation Message:", message)
    #
    #     assert "@" in message, "Expected email validation message not shown"




