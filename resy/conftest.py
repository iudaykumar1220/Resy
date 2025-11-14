
import pytest
from selenium import webdriver

url="https://resy.com/?date=2025-09-05&seats=2"
@pytest.fixture()
def setup_teardown(request):
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    request.cls.driver=driver
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()