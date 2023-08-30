import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from uitility.utils import Util




def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption('browser')

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    if browser == "chrome":
        service_path = Service("E:\selenium\chromedriver-win32\chromedriver.exe")
        driver = webdriver.Chrome(service=service_path, options=chrome_options)
    elif browser == "firefox":
        service_obj = Service("E:\selenium\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    else:
        raise ValueError("Invalid browser name specified")

    driver.implicitly_wait(5)
    driver.get(Util.url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
