import time

from selenium.webdriver.common.by import By


class Homepage:
    menubuttton_id = (By.ID, 'react-burger-menu-btn')
    product_linktext = (By.LINK_TEXT, 'Sauce Labs Backpack')
    def __init__(self, driver):
        self.driver = driver



    def selectProduct(self):
        self.driver.find_element(*Homepage.product_linktext).click()

