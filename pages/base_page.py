"""
Base Page Object Model class with common methods
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from config.config import Config
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.actions = ActionChains(driver)
    
    def navigate_to(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)
        time.sleep(1)  # Wait for page to stabilize
    
    def find_element(self, locator, timeout=Config.EXPLICIT_WAIT):
        """Find element with explicit wait"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise NoSuchElementException(f"Element {locator} not found within {timeout} seconds")
    
    def find_elements(self, locator, timeout=Config.EXPLICIT_WAIT):
        """Find multiple elements with explicit wait"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []
    
    def click(self, locator, timeout=Config.EXPLICIT_WAIT):
        """Click on element with wait"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def type_text(self, locator, text, timeout=Config.EXPLICIT_WAIT):
        """Type text into input field"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator, timeout=Config.EXPLICIT_WAIT):
        """Get text from element"""
        element = self.find_element(locator, timeout)
        return element.text
    
    def is_element_visible(self, locator, timeout=5):
        """Check if element is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator, timeout=5):
        """Check if element is present in DOM"""
        try:
            self.find_element(locator, timeout)
            return True
        except NoSuchElementException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=Config.EXPLICIT_WAIT):
        """Wait for element to disappear"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator):
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
    
    def take_screenshot(self, name):
        """Take screenshot"""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filepath = os.path.join(Config.SCREENSHOTS_DIR, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(filepath)
        return filepath
    
    def get_page_load_time(self):
        """Get page load time using Navigation Timing API"""
        navigation_start = self.driver.execute_script("return window.performance.timing.navigationStart")
        load_complete = self.driver.execute_script("return window.performance.timing.loadEventEnd")
        return (load_complete - navigation_start) / 1000.0  # Convert to seconds
    def dismiss_cookie_banner(self):
    """Dismiss cookie consent banner if present - Updated 2025 version"""
    from selenium.webdriver.common.by import By
    import time

    try:
        # Sélecteur principal 2025 : bouton "Accept All" ou "Dismiss"
        accept_btn = (By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'dismiss')]")
        
        # Sélecteur alternatif : croix de fermeture du welcome banner
        close_btn = (By.CSS_SELECTOR, "button.close-dialog, button[aria-label*='Close'], mat-icon[svgicon='times']")

        # Essai 1 : Accept All / Dismiss
        if self.is_element_visible(accept_btn, timeout=6):
            self.click(accept_btn)
            time.sleep(1)
            print("Cookie banner dismissed (Accept/Dismiss button)")
            return True

        # Essai 2 : Croix de fermeture
        if self.is_element_visible(close_btn, timeout=6):
            self.click(close_btn)
            time.sleep(1)
            print("Cookie banner dismissed (Close button)")
            return True

    except Exception as e:
        print(f"Cookie banner not found or already closed: {e}")

    return False
    