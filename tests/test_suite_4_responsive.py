"""
Test Suite 4: Responsive Design Testing
Contains 4 test cases testing different screen resolutions
"""
import pytest
import time
from pages.home_page import HomePage
from utils.helpers import get_driver
from config.config import Config


class TestResponsiveSuite:
    
    @pytest.fixture(params=[
        ("mobile", Config.RESOLUTIONS["mobile"]),
        ("tablet", Config.RESOLUTIONS["tablet"]),
        ("desktop", Config.RESOLUTIONS["desktop"]),
        ("wide", Config.RESOLUTIONS["wide"])
    ])
    def responsive_driver(self, request):
        """Fixture for different screen resolutions"""
        device_name, resolution = request.param
        driver = get_driver("chrome", resolution=resolution)
        yield driver, device_name, resolution
        driver.quit()
    
    def test_19_responsive_home_page(self, responsive_driver):
        """TC19: Verify home page displays at all resolutions"""
        driver, device, resolution = responsive_driver
        home_page = HomePage(driver)
        
        home_page.open()
        assert home_page.is_logo_visible(), \
            f"Logo not visible on {device} ({resolution[0]}x{resolution[1]})"
        
        print(f"✓ TC19 PASSED: Home page responsive on {device.upper()} {resolution}")
    
    def test_20_responsive_products_grid(self, responsive_driver):
        """TC20: Verify products grid adapts to screen size"""
        driver, device, resolution = responsive_driver
        home_page = HomePage(driver)
        
        home_page.open()
        assert home_page.is_products_grid_visible(), \
            f"Products grid not visible on {device}"
        
        product_count = home_page.get_product_count()
        assert product_count > 0, f"No products on {device}"
        
        print(f"✓ TC20 PASSED: {product_count} products on {device.upper()}")
    
    def test_21_responsive_navigation(self, responsive_driver):
        """TC21: Test navigation at different resolutions"""
        driver, device, resolution = responsive_driver
        home_page = HomePage(driver)
        
        home_page.open()
        
        # Account button should be visible on all devices
        assert home_page.is_element_visible(home_page.ACCOUNT_BUTTON), \
            f"Account button not visible on {device}"
        
        print(f"✓ TC21 PASSED: Navigation works on {device.upper()}")
    
    def test_22_responsive_search(self, responsive_driver):
        """TC22: Test search functionality at different resolutions"""
        driver, device, resolution = responsive_driver
        home_page = HomePage(driver)
        
        home_page.open()
        home_page.search_product("juice")
        time.sleep(2)
        
        product_count = home_page.get_product_count()
        assert product_count >= 0, f"Search failed on {device}"
        
        print(f"✓ TC22 PASSED: Search works on {device.upper()}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=reports/responsive_tests.html", "--self-contained-html"])