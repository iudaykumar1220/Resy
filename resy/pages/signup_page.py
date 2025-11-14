import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class SignupPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        #locators for login
        self.login_email=(By.XPATH,"//input[@id='email']")
        self.login_password=(By.XPATH,"//input[@id='password']")
        self.login_continue=(By.XPATH,"//button[@class='Button Button--primary Button--lg']")

        # Locators for create account
        self.login_btn = (By.XPATH,"//button[normalize-space()='Log in']")
        self.signup_btn = (By.XPATH,"//button[@id='sign-up-button']")
        self.phone_input = (By.XPATH,"//input[@id='phone']")
        self.captcha_box = (By.XPATH,"//div[@class='AuthContainer']")
        self.continue_btn = (By.XPATH,"//button[normalize-space()='Continue']")
        self.otp = (By.XPATH,"//div[@class='InputCode__Field-container']/input")
        self.firstname = (By.XPATH,"//input[@id='first_name']")
        self.lastname = (By.XPATH, "//input[@id='last_name']")
        self.email = (By.XPATH, "//input[@id='email']")
        self.marketing_checkbox = (By.ID, "marketing_opt_in_not_us")
        self.terms_checkbox = (By.ID, "terms_of_service")
        self.second_captcha = (By.XPATH,"//div[@id='captcha__container']")
        self.error_msgs=(By.XPATH,"//div[@class='Form__Error_Inline']")
        self.create_account_btn = (By.XPATH, "//button[normalize-space()='Create Account']")


    # Actions
    def click_login(self):
        self.wait.until(EC.presence_of_element_located(self.login_btn)).click()

    def click_signup(self):
        sign_btn=self.wait.until(EC.presence_of_element_located(self.signup_btn))
        sign_btn.click()

    def enter_phone(self, num):
        self.driver.find_element(*self.phone_input).send_keys(num)
        time.sleep(10)

    def wait_until_captcha_solved(self):
        print("Waiting for captcha to be solved manually")
        self.wait.until(EC.presence_of_element_located(self.captcha_box))
        print("Captcha solved")

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_btn)).click()

    def enter_otp_manually(self):
        otp = input("Enter OTP received: ")
        otp_field = self.wait.until(EC.visibility_of_element_located(self.otp))
        otp_field.clear()
        otp_field.send_keys(otp)

    # def click_create_account(self):
    #     self.wait.until(EC.presence_of_element_located(self.create_account)).click()

    # Corrected method names for clarity
    def enter_first_name(self, name):
        self.driver.find_element(*self.firstname).send_keys(name)

    def enter_last_name(self, last):
        self.driver.find_element(*self.lastname).send_keys(last)

    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def click_marketing_checkbox(self):
        checkbox = self.wait.until(EC.presence_of_element_located(self.marketing_checkbox))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        try:
            checkbox.click()
        except:
            self.driver.execute_script("arguments[0].click();", checkbox)

    def click_terms_checkbox(self):
        try:
            terms = self.wait.until(EC.presence_of_element_located(self.terms_checkbox))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", terms)
            try:
                terms.click()
            except:
                self.driver.execute_script("arguments[0].click();", terms)
        except:
            print("Terms checkbox not found or not clickable")


    def click_submit(self):
        try:
            subs = self.wait.until(EC.element_to_be_clickable(self.create_account_btn))
            subs.click()
        except:
            print("Submit button not found or not clickable")


    def get_error_messages(self):
        elements = self.driver.find_elements(*self.error_msgs)
        messages = []
        for e in elements:
            messages.append(e.text)
        return messages

    # def fill_form(self, name="", lastname="", email=""):
    #     if name:
    #         self.wait.until(EC.presence_of_element_located(self.firstname)).send_keys(name)
    #     if lastname:
    #         self.wait.until(EC.presence_of_element_located(self.lastname)).send_keys(lastname)
    #     if email:
    #         self.wait.until(EC.presence_of_element_located(self.email)).send_keys(email)

    # def wait_until_recaptcha_solved(self):
    #     print("Please solve the reCAPTCHA manually...")
    #     # Wait up to 2 minutes for user to solve it manually
    #     WebDriverWait(self.driver, 120).until(
    #         lambda driver: "recaptcha" not in driver.page_source.lower()
    #     )
    #     print("✅ reCAPTCHA solved successfully, continuing...")


