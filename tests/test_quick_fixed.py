"""
Quick test to verify setup works
Run this first: pytest tests/test_quick_fixed.py -v -s
"""
import pytest
import time
from pages.home_page import HomePage
from utils.helpers import get_driver


def test_basic_homepage():
    """Simple test to verify homepage loads"""
    print("\n🔄 Starting browser...")
    driver = get_driver("chrome")
    
    try:
        print("🌐 Opening OWASP Juice Shop...")
        home_page = HomePage(driver)
        home_page.open()
        
        print("✅ Checking if page loaded...")
        assert home_page.is_products_grid_visible(), "Products grid should be visible"
        
        print("✅ TEST PASSED! Setup is working!")
        
    finally:
        print("🔄 Closing browser...")
        driver.quit()


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])