from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url is incorrect"

    def should_be_login_form(self):
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_form.send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_form.send_keys(password)
        password_confirm_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        password_confirm_form.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        register_button.click()
