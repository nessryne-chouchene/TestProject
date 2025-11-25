"""
Test Suite 3: Cross-Browser Testing
Tests application on Chrome, Firefox, and Edge
"""
import pytest
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.helpers import get_driver
from config.config import Config


class TestCrossBrowserSuite:
    
    @pytest.fixture(params=["chrome", "firefox", "edge"])
    def browser_driver(self, request):
        """Fixture to run tests on multiple browsers"""
        browser = request.param
        driver = get_driver(browser)
        yield driver, browser
        driver.quit()
    
    def test_28_home_page_loads_all_browsers(self, browser_driver):
        """TC28: Verify home page loads on all browsers"""
        driver, browser = browser_driver
        home_page = HomePage(driver)
        
        home_page.open()
        assert home_page.is_logo_visible(), f"Logo not visible on {browser}"
        assert home_page.is_products_grid_visible(), \
            f"Products grid not visible on {browser}"
        
        print(f"✓ TC28 PASSED: Home page loads successfully on {browser.upper()}")
    
    def test_29_search_functionality_all_browsers(self, browser_driver):
        """TC29: Test search functionality across browsers"""
        driver, browser = browser_driver
        home_page = HomePage(driver)
        
        home_page.open()
        home_page.search_product("apple")
        time.sleep(2)
        
        product_count = home_page.get_product_count()
        assert product_count > 0, f"Search failed on {browser}"
        
        print(f"✓ TC29 PASSED: Search works on {browser.upper()} - {product_count} products")
    
    def test_30_navigation_all_browsers(self, browser_driver):
        """TC30: Test navigation across browsers"""
        driver, browser = browser_driver
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        home_page.open()
        home_page.click_account()
        time.sleep(1)
        home_page.click_login()
        time.sleep(1)
        
        assert login_page.is_element_visible(login_page.EMAIL_INPUT), \
            f"Navigation failed on {browser}"
        
        print(f"✓ TC30 PASSED: Navigation works on {browser.upper()}")
    
    def test_31_cart_button_all_browsers(self, browser_driver):
        """TC31: Verify cart button visibility across browsers"""
        driver, browser = browser_driver
        home_page = HomePage(driver)
        
        home_page.open()
        assert home_page.is_element_visible(home_page.CART_BUTTON), \
            f"Cart button not visible on {browser}"
        
        print(f"✓ TC31 PASSED: Cart button visible on {browser.upper()}")
    
    def test_32_side_menu_all_browsers(self, browser_driver):
        """TC32: Test side menu across browsers"""
        driver, browser = browser_driver
        home_page = HomePage(driver)
        
        home_page.open()
        home_page.click_side_menu()
        time.sleep(1)
        
        from selenium.webdriver.common.by import By
        side_menu = (By.CSS_SELECTOR, "mat-sidenav")
        assert home_page.is_element_visible(side_menu, timeout=5), \
            f"Side menu failed on {browser}"
        
        print(f"✓ TC32 PASSED: Side menu works on {browser.upper()}")
    
    @pytest.mark.parametrize("browser_name", ["chrome"])
    def test_33_login_form_validation_chrome(self, browser_name):
        """TC33: Test login form validation (Chrome specific)"""
        driver = get_driver(browser_name)
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        try:
            home_page.open()
            home_page.click_account()
            time.sleep(1)
            home_page.click_login()
            time.sleep(1)
            
            login_page.enter_email("invalid-email")
            login_page.enter_password("test")
            
            login_btn = login_page.find_element(login_page.LOGIN_BUTTON)
            assert not login_btn.is_enabled(), "Validation failed"
            
            print(f"✓ TC33 PASSED: Form validation works on Chrome")
        finally:
            driver.quit()


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=reports/cross_browser_tests.html"])