from selenium.webdriver.common.by import By


class CheckoutConfirm:
    def __init__(self,driver):
        self.driver = driver
        self.confirmbutton_id = (By.ID,"finish")

    def click_on_confirm_button(self):
        self.driver.find_element(*self.confirmbutton_id).click()
