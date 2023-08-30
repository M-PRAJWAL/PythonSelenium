from selenium.webdriver.common.by import By
from pages.homepage import Homepage


class Logout(Homepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver =driver
        self.logoutbutton_id = (By.ID,'logout_sidebar_link')

    def logout(self):
        self.driver.find_element(*Homepage.menubuttton_id).click()  #Inheritence
        self.driver.find_element(*self.logoutbutton_id).click()

