from selenium.webdriver.common.by import By


class CheckoutSuccess:
    def __init__(self,driver):
        self.driver = driver
        self.backbutton_id = (By.ID,"back-to-products")

    def click_on_back_to_home(self):
        self.driver.find_element(*self.backbutton_id).click()