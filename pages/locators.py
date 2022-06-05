from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_SUCCESS_ADDED_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    ALERT_INFO_BASKET_TOTAL_COST = (By.CSS_SELECTOR, ".alert:nth-child(3) p:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
