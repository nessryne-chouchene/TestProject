"""
Home Page Object Model - FIXED VERSION
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time


class HomePage(BasePage):
    # Locators - FIXED to match actual OWASP Juice Shop elements
    ACCOUNT_BUTTON = (By.XPATH, "//button[@id='navbarAccount'] | //span[contains(text(), 'Account')]")
    LOGIN_BUTTON = (By.ID, "navbarLoginButton")
    
    # Search elements - FIXED
    SEARCH_BUTTON = (By.ID, "searchQuery")
    SEARCH_ICON = (By.XPATH, "//mat-icon[contains(text(), 'search')]")
    
    # Other elements
    PRODUCTS_GRID = (By.CSS_SELECTOR, ".mat-grid-list, mat-grid-list")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "mat-card.mat-card, mat-grid-tile")
    CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='Show shopping cart'], button[aria-label*='cart']")
    COOKIE_DISMISS = (By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'dismiss')]")
    WELCOME_BANNER_DISMISS = (By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner'], .close-dialog")
    LOGO = (By.CSS_SELECTOR, "img[alt*='OWASP'], img[src*='JuiceShop'], .mat-toolbar img")
    SIDE_MENU_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='Open'], button.mat-button[aria-label*='menu']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        """Open home page and wait for it to load"""
        self.navigate_to("https://demo.owasp-juice.shop/#/")
        time.sleep(3)  # Wait for Angular to load
        self.dismiss_initial_popups()
        time.sleep(2)  # Extra wait after dismissing popups
    
    def dismiss_initial_popups(self):
        """Dismiss welcome banner and cookie consent"""
        try:
            # Dismiss welcome banner
            if self.is_element_visible(self.WELCOME_BANNER_DISMISS, timeout=5):
                self.click(self.WELCOME_BANNER_DISMISS)
                time.sleep(1)
        except Exception as e:
            print(f"No welcome banner or already dismissed: {e}")
        
        try:
            # Dismiss cookie banner  
            if self.is_element_visible(self.COOKIE_DISMISS, timeout=5):
                self.click(self.COOKIE_DISMISS)
                time.sleep(1)
        except Exception as e:
            print(f"No cookie banner or already dismissed: {e}")
    
    def click_account(self):
        """Click account button"""
        time.sleep(1)
        self.click(self.ACCOUNT_BUTTON)
    
    def click_login(self):
        """Click login button"""
        time.sleep(1)
        self.click(self.LOGIN_BUTTON)
    
    def search_product(self, product_name):
        """
        Search for a product - FIXED VERSION
        Uses direct input to search field
        """
        try:
            # Wait for page to be ready
            time.sleep(2)
            
            # Find and click the search field directly
            search_field = self.find_element(self.SEARCH_BUTTON, timeout=10)
            
            # Click to focus
            search_field.click()
            time.sleep(1)
            
            # Clear any existing text
            search_field.clear()
            time.sleep(0.5)
            
            # Type the search term
            search_field.send_keys(product_name)
            time.sleep(1)
            
            # Press Enter
            search_field.send_keys(Keys.RETURN)
            time.sleep(2)
            
        except Exception as e:
            print(f"Search failed: {e}")
            # Alternative: Try clicking search icon first
            try:
                self.click(self.SEARCH_ICON)
                time.sleep(1)
                search_field = self.find_element(self.SEARCH_BUTTON)
                search_field.send_keys(product_name)
                search_field.send_keys(Keys.RETURN)
                time.sleep(2)
            except:
                raise Exception(f"Could not perform search: {e}")
    
    def get_product_count(self):
        """Get number of products displayed"""
        try:
            time.sleep(2)  # Wait for products to load
            products = self.find_elements(self.PRODUCT_CARDS, timeout=10)
            return len(products)
        except:
            return 0
    
    def is_products_grid_visible(self):
        """Check if products grid is visible"""
        time.sleep(2)
        return self.is_element_visible(self.PRODUCTS_GRID, timeout=10)
    
    def click_cart(self):
        """Click shopping cart button"""
        time.sleep(1)
        self.click(self.CART_BUTTON)
    
    def click_side_menu(self):
        """Click side menu button"""
        time.sleep(1)
        self.click(self.SIDE_MENU_BUTTON)
    
    def is_logo_visible(self):
        """Check if logo is visible"""
        time.sleep(1)
        return self.is_element_visible(self.LOGO, timeout=10)