import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
## chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == "chrome":
        service_obj = Service("E:\selenium")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    elif browser_name == "firefox":
        service_obj = Service("E:\selenium")
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
