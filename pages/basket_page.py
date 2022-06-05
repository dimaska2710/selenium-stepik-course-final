from pages.main_page import MainPage
from pages.locators import BasketPageLocators


class BasketPage(MainPage):

    def should_contain_emptiness_info_text(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        assert "Your basket is empty" in text, "Empty basket doesn't contain emptiness into text"

    def should_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_NOW), "Basket is not empty"
