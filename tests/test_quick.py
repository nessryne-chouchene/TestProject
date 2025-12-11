"""
Quick test to verify setup
"""
import pytest
from pages.home_page import HomePage
from utils.helpers import get_driver


def test_basic_setup():
    """Quick test to verify everything works"""
    driver = get_driver("chrome")
    try:
        home_page = HomePage(driver)
        home_page.open()
        assert home_page.is_logo_visible(), "Logo should be visible"
        print("✅ TEST PASSED: Setup is working!")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_basic_setup()