"""
Login Page Object Model
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    REMEMBER_ME_CHECKBOX = (By.ID, "rememberMe-input")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='#/forgot-password']")
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='#/register']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error")
    GOOGLE_LOGIN_BUTTON = (By.ID, "loginButtonGoogle")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_email(self, email):
        """Enter email address"""
        self.type_text(self.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        """Enter password"""
        self.type_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
        time.sleep(2)  # Wait for login process
    
    def check_remember_me(self):
        """Check remember me checkbox"""
        checkbox = self.find_element(self.REMEMBER_ME_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()
    
    def login(self, email, password, remember=False):
        """Complete login process"""
        self.enter_email(email)
        self.enter_password(password)
        if remember:
            self.check_remember_me()
        self.click_login_button()
    
    def is_error_message_displayed(self):
        """Check if error message is displayed"""
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=5)
    
    def get_error_message(self):
        """Get error message text"""
        if self.is_error_message_displayed():
            return self.get_text(self.ERROR_MESSAGE)
        return None
    
    def click_register_link(self):
        """Click registration link"""
        self.click(self.REGISTER_LINK)
    
    def click_forgot_password(self):
        """Click forgot password link"""
        self.click(self.FORGOT_PASSWORD_LINK)