from pages.main_page import MainPage
from pages.locators import ProductPageLocators


class ProductPage(MainPage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return float(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:])

    def get_alert_success_added_to_basket(self):
        return self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_ADDED_TO_BASKET_PRODUCT_NAME).text

    def get_alert_info_basket_total_cost(self):
        return float(self.browser.find_element(*ProductPageLocators.ALERT_INFO_BASKET_TOTAL_COST).text[1:])

    def should_have_correct_name_in_message(self):
        assert self.get_alert_success_added_to_basket() == self.get_product_name(), \
            "Product name in alert section is not equal to the product name from description"

    def should_have_correct_cost_in_basket(self):
        assert self.get_alert_info_basket_total_cost() == self.get_product_price(), \
            "Basket total price is not equal to the product price"

    def should_have_product_page(self):
        self.should_have_correct_name_in_message()
        self.should_have_correct_cost_in_basket()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Element should have disappeared, but it have not"
