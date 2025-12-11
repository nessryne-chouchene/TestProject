"""
Registration Page Object Model
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class RegistrationPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.ID, "emailControl")
    PASSWORD_INPUT = (By.ID, "passwordControl")
    REPEAT_PASSWORD_INPUT = (By.ID, "repeatPasswordControl")
    SECURITY_QUESTION_DROPDOWN = (By.NAME, "securityQuestion")
    SECURITY_ANSWER_INPUT = (By.ID, "securityAnswerControl")
    REGISTER_BUTTON = (By.ID, "registerButton")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_email(self, email):
        """Enter email address"""
        self.type_text(self.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        """Enter password"""
        self.type_text(self.PASSWORD_INPUT, password)
    
    def enter_repeat_password(self, password):
        """Enter repeat password"""
        self.type_text(self.REPEAT_PASSWORD_INPUT, password)
    
    def select_security_question(self, question_index):
        """Select security question by index"""
        dropdown = self.find_element(self.SECURITY_QUESTION_DROPDOWN)
        dropdown.click()
        time.sleep(0.5)
    
    def enter_security_answer(self, answer):
        """Enter security answer"""
        self.type_text(self.SECURITY_ANSWER_INPUT, answer)
    
    def click_register(self):
        """Click register button"""
        self.click(self.REGISTER_BUTTON)
        time.sleep(2)
