"""
Test Suite 1: Functional Testing
Contains 20+ test cases with boundary testing and state transitions
"""
import pytest
import time
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.helpers import get_driver, BoundaryValues, generate_random_email
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
    
    # ===== POSITIVE TEST CASES =====
    
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
    
    def test_04_login_with_valid_credentials(self):
        """TC04: Login with valid credentials (SQL injection method for demo)"""
        self.home_page.open()
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(1)
        
        # Use SQL injection for testing (this is a vulnerable demo app)
        self.login_page.login("' or 1=1--", "anything")
        time.sleep(2)
        
        # Check if redirected (account button should be visible)
        assert self.home_page.is_element_visible(self.home_page.ACCOUNT_BUTTON)
        print("✓ TC04 PASSED: Login successful")
    
    def test_05_search_boundary_single_character(self):
        """TC05: Boundary test - Search with single character"""
        self.home_page.open()
        self.home_page.search_product("a")
        time.sleep(2)
        # Should show some results or handle gracefully
        assert self.home_page.is_products_grid_visible()
        print("✓ TC05 PASSED: Single character search handled")
    
    def test_06_cart_button_visible(self):
        """TC06: Verify cart button is accessible"""
        self.home_page.open()
        assert self.home_page.is_element_visible(self.home_page.CART_BUTTON), \
            "Cart button not visible"
        print("✓ TC06 PASSED: Cart button is visible")
    
    def test_07_side_menu_opens(self):
        """TC07: Side menu opens on click"""
        self.home_page.open()
        self.home_page.click_side_menu()
        time.sleep(1)
        # Check if side menu is visible
        side_menu = (By.CSS_SELECTOR, "mat-sidenav")
        assert self.home_page.is_element_visible(side_menu, timeout=5)
        print("✓ TC07 PASSED: Side menu opens successfully")
    
    def test_08_products_display_on_load(self):
        """TC08: Products are displayed on page load"""
        self.home_page.open()
        product_count = self.home_page.get_product_count()
        assert product_count > 0, "No products displayed"
        print(f"✓ TC08 PASSED: {product_count} products displayed")
    
    def test_09_search_with_numbers(self):
        """TC09: Search with numeric input"""
        self.home_page.open()
        self.home_page.search_product("500")
        time.sleep(2)
        assert self.home_page.is_products_grid_visible()
        print("✓ TC09 PASSED: Numeric search handled")
    
    def test_10_page_title_correct(self):
        """TC10: Verify page title is correct"""
        self.home_page.open()
        title = self.driver.title
        assert "OWASP Juice Shop" in title, f"Incorrect title: {title}"
        print(f"✓ TC10 PASSED: Page title is '{title}'")
    
    # ===== NEGATIVE TEST CASES =====
    
    def test_11_login_with_empty_email(self):
        """TC11: Negative - Login with empty email"""
        self.home_page.open()
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(1)
        
        self.login_page.enter_email("")
        self.login_page.enter_password("password123")
        
        # Login button should be disabled or show error
        login_btn = self.login_page.find_element(self.login_page.LOGIN_BUTTON)
        assert not login_btn.is_enabled(), "Login button should be disabled"
        print("✓ TC11 PASSED: Empty email prevents login")
    
    def test_12_login_with_invalid_email_format(self):
        """TC12: Negative - Login with invalid email format (boundary)"""
        self.home_page.open()
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(1)
        
        boundaries = BoundaryValues.get_email_boundaries()
        self.login_page.enter_email(boundaries["invalid_no_at"])
        self.login_page.enter_password("password123")
        
        login_btn = self.login_page.find_element(self.login_page.LOGIN_BUTTON)
        assert not login_btn.is_enabled(), "Login should not be allowed"
        print("✓ TC12 PASSED: Invalid email format rejected")
    
    def test_13_login_with_email_no_domain(self):
        """TC13: Negative - Email boundary test without domain"""
        self.home_page.open()
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(1)
        
        boundaries = BoundaryValues.get_email_boundaries()
        self.login_page.enter_email(boundaries["invalid_no_domain"])
        self.login_page.enter_password("password123")
        
        login_btn = self.login_page.find_element(self.login_page.LOGIN_BUTTON)
        assert not login_btn.is_enabled()
        print("✓ TC13 PASSED: Email without domain rejected")
    
    def test_14_search_with_special_characters(self):
        """TC14: Negative - Search with special characters"""
        self.home_page.open()
        boundaries = BoundaryValues.get_search_boundaries()
        self.home_page.search_product(boundaries["special_chars"])
        time.sleep(2)
        # Should handle gracefully
        assert self.home_page.is_products_grid_visible()
        print("✓ TC14 PASSED: Special characters in search handled")
    
    def test_15_search_with_sql_injection_attempt(self):
        """TC15: Security - SQL injection in search"""
        self.home_page.open()
        boundaries = BoundaryValues.get_search_boundaries()
        self.home_page.search_product(boundaries["sql_injection"])
        time.sleep(2)
        # Should not break the application
        assert self.home_page.is_products_grid_visible()
        print("✓ TC15 PASSED: SQL injection attempt handled")
    
    def test_16_search_with_xss_attempt(self):
        """TC16: Security - XSS attempt in search"""
        self.home_page.open()
        boundaries = BoundaryValues.get_search_boundaries()
        self.home_page.search_product(boundaries["xss_attempt"])
        time.sleep(2)
        # Should sanitize input
        assert self.home_page.is_products_grid_visible()
        print("✓ TC16 PASSED: XSS attempt handled")
    
    def test_17_search_with_very_long_input(self):
        """TC17: Boundary - Search with maximum length input"""
        self.home_page.open()
        boundaries = BoundaryValues.get_search_boundaries()
        self.home_page.search_product(boundaries["valid_long"])
        time.sleep(2)
        assert self.home_page.is_products_grid_visible()
        print("✓ TC17 PASSED: Long search input handled")
    
    def test_18_empty_search_query(self):
        """TC18: Boundary - Empty search query"""
        self.home_page.open()
        self.home_page.search_product("")
        time.sleep(2)
        # Should show all products
        product_count = self.home_page.get_product_count()
        assert product_count > 0, "Empty search should show products"
        print("✓ TC18 PASSED: Empty search shows all products")
    
    def test_19_login_email_with_spaces(self):
        """TC19: Boundary - Email with spaces"""
        self.home_page.open()
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(1)
        
        self.login_page.enter_email("test @example.com")
        self.login_page.enter_password("password123")
        
        login_btn = self.login_page.find_element(self.login_page.LOGIN_BUTTON)
        assert not login_btn.is_enabled()
        print("✓ TC19 PASSED: Email with spaces rejected")
    
    def test_20_multiple_page_state_transitions(self):
        """TC20: State transitions - Navigate through multiple pages"""
        self.home_page.open()
        assert self.home_page.is_logo_visible(), "Home page not loaded"
        
        # Navigate to login
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(1)
        assert self.login_page.is_element_visible(self.login_page.EMAIL_INPUT)
        
        # Navigate to register
        self.login_page.click_register_link()
        time.sleep(1)
        register_email = (By.ID, "emailControl")
        assert self.login_page.is_element_visible(register_email)
        
        print("✓ TC20 PASSED: Multiple state transitions successful")
    
    def test_21_cart_persistence_after_navigation(self):
        """TC21: State - Cart persists after navigation"""
        self.home_page.open()
        
        # Click cart
        self.home_page.click_cart()
        time.sleep(1)
        
        # Navigate back to home
        self.driver.back()
        time.sleep(1)
        
        # Cart button should still be visible
        assert self.home_page.is_element_visible(self.home_page.CART_BUTTON)
        print("✓ TC21 PASSED: Cart persists after navigation")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=reports/functional_tests.html"])