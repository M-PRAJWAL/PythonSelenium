import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

from Baseclass import Baseclass
from pageObject.Homepage import Homepage


# @pytest.mark.usefixtures("setup")
class TestOne(Baseclass):
    def test_e2e(self):
        home = Homepage(self.driver)
        home.shopitem().click()
        self.driver.find_element(By.CSS_SELECTOR, "a[href*= 'shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, "div h4 a").text
            if product_name == "Blackberry":
                product.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-info']").click()

        self.driver.find_element(By.CSS_SELECTOR, 'a[class = "nav-link btn btn-primary"]').click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class = 'btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CSS_SELECTOR, "div [class = 'checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
        success = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in success
