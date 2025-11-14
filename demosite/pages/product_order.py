from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class OrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.search_bar=(By.XPATH,"//input[@placeholder='Search']")
        self.search_btn=(By.XPATH,"//button[@class='btn btn-default btn-lg']")


    def search_item(self,name):
        search=self.wait.until(EC.presence_of_element_located(self.search_bar))
        self.driver.execute_script("arguments[0].scrollIntoView(true)",search)
        search.send_keys(name)

    def search_click(self):
        button=self.wait.until(EC.presence_of_element_located(self.search_btn))
        button.click()


