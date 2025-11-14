import pytest
from selenium import webdriver


url="https://tutorialsninja.com/demo/"
@pytest.fixture()
def fixture_method(request):
    driver=webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()