from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class Signin:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators
        self.loc_my_account = (By.XPATH, "//span[text()='My Account']")
        self.loc_register = (By.XPATH, "//a[text()='Register']")
        self.loc_first_name = (By.ID, "input-firstname")
        self.loc_last_name = (By.ID, "input-lastname")
        self.loc_email = (By.ID, "input-email")
        self.loc_phone = (By.ID, "input-telephone")
        self.loc_password = (By.ID, "input-password")
        self.loc_confirm_password = (By.ID, "input-confirm")
        self.loc_agree_terms = (By.NAME, "agree")
        self.loc_continue_btn = (By.XPATH, "//input[@value='Continue']")
        self.loc_error=(By.XPATH,"//div[@class='text-danger']")

    # Click actions
    def click_my_account(self):
        account = self.wait.until(EC.element_to_be_clickable(self.loc_my_account))
        account.click()

    def click_register(self):
        register = self.wait.until(EC.element_to_be_clickable(self.loc_register))
        register.click()

    # Input fields
    def enter_first_name(self, fname):
        firstname = self.wait.until(EC.presence_of_element_located(self.loc_first_name))
        firstname.clear()
        firstname.send_keys(fname)

    def enter_last_name(self, lname):
        lastname = self.wait.until(EC.presence_of_element_located(self.loc_last_name))
        lastname.clear()
        lastname.send_keys(lname)

    def enter_email(self, mail):
        email = self.wait.until(EC.presence_of_element_located(self.loc_email))
        email.clear()
        email.send_keys(mail)

    def enter_phone(self, num):
        phone = self.wait.until(EC.presence_of_element_located(self.loc_phone))
        phone.clear()
        phone.send_keys(num)

    def enter_password(self, pasw):
        password = self.wait.until(EC.presence_of_element_located(self.loc_password))
        password.clear()
        password.send_keys(pasw)

    def enter_confirm_password(self, confirm_pw):
        confirm = self.wait.until(EC.presence_of_element_located(self.loc_confirm_password))
        confirm.clear()
        confirm.send_keys(confirm_pw)

    # Checkbox and button
    def agree_terms(self):
        term = self.wait.until(EC.element_to_be_clickable(self.loc_agree_terms))
        term.click()

    def click_continue(self):
        cont_btn = self.wait.until(EC.element_to_be_clickable(self.loc_continue_btn))
        cont_btn.click()

    def all_errors(self):
        reg_errors = self.driver.find_elements(*self.loc_error)
        error_texts = []

        for x in reg_errors:
            if x.is_displayed():
                text = x.text.strip()
                print(text)
                error_texts.append(text)
            else:
                print("Element not visible")



        return error_texts


