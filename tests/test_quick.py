"""
Quick test to verify setup
"""
import pytest
from pages.home_page import HomePage
from utils.helpers import get_driver
import time


def test_basic_setup():
    """Quick test to verify everything works"""
    driver = get_driver("chrome")
    try:
        print("\n🔧 Starting basic setup test...")
        
        home_page = HomePage(driver)
        print("✅ HomePage object created")
        
        home_page.open()
        print("✅ Page opened")
        
        # Take screenshot for debugging
        home_page.take_screenshot("test_quick_homepage")
        print("✅ Screenshot taken")
        
        # Check if page loaded (products visible is a good indicator)
        assert home_page.is_logo_visible(), "Homepage should be loaded (logo or products visible)"
        print("✅ TEST PASSED: Setup is working!")
        
        # Additional checks
        print(f"📊 Products found: {home_page.get_product_count()}")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        home_page.take_screenshot("test_quick_failure")
        raise
    except Exception as e:
        print(f"❌ Error during test: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_basic_setup()