"""
Test Suite 3: Cross-Browser Testing
Contains 4 test cases testing on Chrome, Firefox, and Edge
"""
import pytest
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.helpers import get_driver


class TestCrossBrowserSuite:
    
    @pytest.fixture(params=["chrome", "firefox", "edge"])
    def browser_driver(self, request):
        """Fixture to run tests on multiple browsers"""
        browser = request.param
        driver = get_driver(browser)
        yield driver, browser
        driver.quit()
    
    def test_15_home_page_all_browsers(self, browser_driver):
        """TC15: Verify home page loads on all browsers"""
        driver, browser = browser_driver
        home_page = HomePage(driver)
        
        home_page.open()
        assert home_page.is_logo_visible(), f"Logo not visible on {browser}"
        assert home_page.is_products_grid_visible(), \
            f"Products grid not visible on {browser}"
        
        print(f"✓ TC15 PASSED: Home page works on {browser.upper()}")
    
    def test_16_search_all_browsers(self, browser_driver):
        """TC16: Test search functionality across browsers"""
        driver, browser = browser_driver
        home_page = HomePage(driver)
        
        home_page.open()
        home_page.search_product("apple")
        time.sleep(2)
        
        product_count = home_page.get_product_count()
        assert product_count > 0, f"Search failed on {browser}"
        
        print(f"✓ TC16 PASSED: Search works on {browser.upper()} - {product_count} products")
    
    def test_17_navigation_all_browsers(self, browser_driver):
        """TC17: Test navigation across browsers"""
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
        
        print(f"✓ TC17 PASSED: Navigation works on {browser.upper()}")
    
    def test_18_cart_all_browsers(self, browser_driver):
        """TC18: Verify cart button across browsers"""
        driver, browser = browser_driver
        home_page = HomePage(driver)
        
        home_page.open()
        assert home_page.is_element_visible(home_page.CART_BUTTON), \
            f"Cart button not visible on {browser}"
        
        print(f"✓ TC18 PASSED: Cart button visible on {browser.upper()}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=reports/cross_browser_tests.html", "--self-contained-html"])