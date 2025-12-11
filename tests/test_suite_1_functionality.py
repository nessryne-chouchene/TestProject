"""
Test Suite 1: Functional Testing
Contains 10 test cases (5 positive + 5 negative) with boundary testing
"""
import pytest
import time
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.helpers import get_driver, BoundaryValues
from config.config import Config


class TestFunctionalSuite:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup before each test"""
        self.driver = get_driver("chrome")
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()
    
    # ===== POSITIVE TEST CASES (5 tests) =====
    
    def test_01_home_page_loads_successfully(self):
        """TC01: Verify home page loads with all elements"""
        self.home_page.open()
        assert self.home_page.is_logo_visible(), "Logo not visible"
        assert self.home_page.is_products_grid_visible(), "Products grid not visible"
        print("✓ TC01 PASSED: Home page loaded successfully")
    
    def test_02_search_valid_product(self):
        """TC02: Search for valid product returns results"""
        self.home_page.open()
        self.home_page.search_product("apple")
        time.sleep(2)
        product_count = self.home_page.get_product_count()
        assert product_count > 0, "No products found for valid search"
        print(f"✓ TC02 PASSED: Found {product_count} products")
    
    def test_03_navigate_to_login_page(self):
        """TC03: State transition - Navigate from home to login"""
        self.home_page.open()
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(1)
        assert self.login_page.is_element_visible(self.login_page.EMAIL_INPUT), \
            "Login page not loaded"
        print("✓ TC03 PASSED: Navigation to login page successful")
    
    def test_04_cart_button_accessible(self):
        """TC04: Verify cart button is accessible"""
        self.home_page.open()
        assert self.home_page.is_element_visible(self.home_page.CART_BUTTON), \
            "Cart button not visible"
        print("✓ TC04 PASSED: Cart button is accessible")
    
    def test_05_side_menu_functionality(self):
        """TC05: Side menu opens successfully"""
        self.home_page.open()
        self.home_page.click_side_menu()
        time.sleep(1)
        side_menu = (By.CSS_SELECTOR, "mat-sidenav")
        assert self.home_page.is_element_visible(side_menu, timeout=5), \
            "Side menu not visible"
        print("✓ TC05 PASSED: Side menu opens successfully")
    
    # ===== NEGATIVE TEST CASES (5 tests) =====
    
    def test_06_login_empty_email_boundary(self):
        """TC06: Boundary test - Login with empty email"""
        self.home_page.open()
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(1)
        
        self.login_page.enter_email("")
        self.login_page.enter_password("password123")
        
        login_btn = self.login_page.find_element(self.login_page.LOGIN_BUTTON)
        assert not login_btn.is_enabled(), "Login button should be disabled"
        print("✓ TC06 PASSED: Empty email prevents login")
    
    def test_07_login_invalid_email_format_boundary(self):
        """TC07: Boundary test - Invalid email format"""
        self.home_page.open()
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(1)
        
        boundaries = BoundaryValues.get_email_boundaries()
        self.login_page.enter_email(boundaries["invalid_no_at"])
        self.login_page.enter_password("password123")
        
        login_btn = self.login_page.find_element(self.login_page.LOGIN_BUTTON)
        assert not login_btn.is_enabled(), "Invalid email should prevent login"
        print("✓ TC07 PASSED: Invalid email format rejected")
    
    def test_08_search_special_characters(self):
        """TC08: Negative - Search with special characters"""
        self.home_page.open()
        boundaries = BoundaryValues.get_search_boundaries()
        self.home_page.search_product(boundaries["special_chars"])
        time.sleep(2)
        assert self.home_page.is_products_grid_visible(), \
            "Page should handle special characters"
        print("✓ TC08 PASSED: Special characters handled")
    
    def test_09_search_sql_injection_attempt(self):
        """TC09: Security test - SQL injection in search"""
        self.home_page.open()
        boundaries = BoundaryValues.get_search_boundaries()
        self.home_page.search_product(boundaries["sql_injection"])
        time.sleep(2)
        assert self.home_page.is_products_grid_visible(), \
            "SQL injection should not break application"
        print("✓ TC09 PASSED: SQL injection attempt handled")
    
    def test_10_search_xss_attempt(self):
        """TC10: Security test - XSS attempt in search"""
        self.home_page.open()
        boundaries = BoundaryValues.get_search_boundaries()
        self.home_page.search_product(boundaries["xss_attempt"])
        time.sleep(2)
        assert self.home_page.is_products_grid_visible(), \
            "XSS attempt should be sanitized"
        print("✓ TC10 PASSED: XSS attempt handled")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=reports/functional_tests.html", "--self-contained-html"])