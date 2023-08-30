from selenium.webdriver.common.by import By


class Login:

    def __init__(self,driver):
        self.driver = driver

        self.username_id = (By.ID,"user-name")
        self.password_id = (By.ID,'password')
        self.loginbutton_id = (By.ID,'login-button')
        self.shoppingcardcontainer_id = (By.ID,'shopping_cart_container')

    def username(self, username):
        self.driver.find_element(*self.username_id).clear()
        self.driver.find_element(*self.username_id).send_keys(username)

    def password(self,password):
        self.driver.find_element(*self.password_id).clear()
        self.driver.find_element(*self.password_id).send_keys(password)

    def click_loginbutton(self):
        self.driver.find_element(*self.loginbutton_id).click()

    def sucessAssertion(self):
        success = self.driver.find_element(*self.shoppingcardcontainer_id)
        assert success, "login failed"
