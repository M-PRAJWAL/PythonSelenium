from selenium.webdriver.common.by import By


class Cartpage:
    def __init__(self,driver):
        self.driver = driver
        self.checkoutbutton_id = (By.ID,"checkout")

    def click_checkout_button(self):
        print(self.driver.find_element(*self.checkoutbutton_id).text)
        self.driver.find_element(*self.checkoutbutton_id).click()
