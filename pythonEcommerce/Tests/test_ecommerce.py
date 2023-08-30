import pytest
from selenium.webdriver.common.by import By
from pages.loginpage import Login
from pages.homepage import Homepage
from pages.productDetailpage import PrdoductDetails
from pages.Cartpage import Cartpage
from pages.checckoutpage import Checkoutpage
from pages.checkoutconfirmpage import CheckoutConfirm
from pages.checkoutsuccesspage import CheckoutSuccess
from pages.logout import Logout
from uitility.utils import Util

@pytest.mark.usefixtures("test_setup")

class Test_ecom():
    def test_login(self):
        login = Login(self.driver)
        login.username(Util.username)
        login.password(Util.password)
        login.click_loginbutton()
        login.sucessAssertion()


    def test_selectProduct(self):
        homepage =Homepage(self.driver)
        homepage.selectProduct()

    def test_add_to_Cart(self):
        product = PrdoductDetails(self.driver)
        product.click_add_to_cart()
        product.assert_remove_button()
        product.click_on_cart()

    def test_click_on_checkout(self):
        checkout = Cartpage(self.driver)
        checkout.click_checkout_button()


    def test_fill_checkout_details(self):
        checkoutdetails = Checkoutpage(self.driver)
        checkoutdetails.fill_firstname()
        checkoutdetails.fill_lastname()
        checkoutdetails.fill_postalcode()
        checkoutdetails.click_on_continue()

    def test_checkout_confirm(self):
        confirmcheckout = CheckoutConfirm(self.driver)
        confirmcheckout.click_on_confirm_button()

    def test_checkout_success(self):
        checkoutsuccess = CheckoutSuccess(self.driver)
        checkoutsuccess.click_on_back_to_home()
       
    def test_logout(self):
        logout = Logout(self.driver)
        logout.logout()









