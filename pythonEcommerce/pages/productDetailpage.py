from selenium.webdriver.common.by import By


class PrdoductDetails:
    def __init__(self, driver):
        self.driver = driver
        self.carbutton_id = (By.ID,"add-to-cart-sauce-labs-backpack")
        self.removebtn_id = (By.ID,"remove-sauce-labs-backpack")
        self.cartbutton_class = (By.CLASS_NAME,'shopping_cart_link')

    def click_add_to_cart(self):
        self.driver.find_element(*self.carbutton_id).click()

    def assert_remove_button(self):
        remove_btn = self.driver.find_element(*self.removebtn_id)
        assert remove_btn.text == "Remove"

    def click_on_cart(self):
        self.driver.find_element(*self.cartbutton_class).click()

