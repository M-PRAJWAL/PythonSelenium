from selenium.webdriver.common.by import By


class Checkoutpage:
    def __init__(self,driver):
        self.driver = driver
        self.firstname_id = (By.ID,"first-name")
        self.lastname_id = (By.ID,"last-name")
        self.postalcode_id = (By.ID,"postal-code")
        self.continuebutton_id =By.ID,"continue"


    def fill_firstname(self):
        self.driver.find_element(*self.firstname_id).send_keys("test")
    def fill_lastname(self):
        self.driver.find_element(*self.lastname_id).send_keys("123")
    def fill_postalcode(self):
        self.driver.find_element(*self.postalcode_id).send_keys("123456")
    def click_on_continue(self):
        self.driver.find_element(*self.continuebutton_id).click()
