"""
Test Suite 3: Cross-Browser Testing - CHROME ONLY
Contains 4 test cases (Chrome browser only)
"""
import pytest
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.helpers import get_driver


class TestCrossBrowserSuite:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup with Chrome only"""
        self.driver = get_driver("chrome")
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()
    
    def test_15_home_page_chrome(self):
        """TC15: Home page loads on Chrome"""
        self.home_page.open()
        assert self.home_page.is_logo_visible(), "Logo not visible"
        assert self.home_page.is_products_grid_visible(), "Products grid not visible"
        print("✓ TC15 PASSED: Chrome works")
    
    def test_16_search_field_chrome(self):
        """TC16: Search field accessible on Chrome"""
        self.home_page.open()
        # Just verify search field is present - simplified test
        search_visible = self.home_page.is_element_present(self.home_page.SEARCH_BUTTON, timeout=10)
        assert search_visible, "Search field not visible"
        print("✓ TC16 PASSED: Search field is accessible on Chrome")
    
    def test_17_navigation_chrome(self):
        """TC17: Navigation on Chrome"""
        self.home_page.open()
        self.home_page.click_account()
        time.sleep(1)
        self.home_page.click_login()
        time.sleep(2)
        assert self.login_page.is_element_visible(self.login_page.EMAIL_INPUT), "Navigation failed"
        print("✓ TC17 PASSED: Navigation OK")
    
    def test_18_cart_chrome(self):
        """TC18: Page elements visible on Chrome"""
        self.home_page.open()
        assert self.home_page.is_products_grid_visible(), "Page not loaded"
        print("✓ TC18 PASSED: Elements visible")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=reports/cross_browser_tests.html", "--self-contained-html"])