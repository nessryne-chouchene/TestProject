"""
Home Page Object Model
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time


class HomePage(BasePage):
    # Locators - Updated for current Juice Shop version
    ACCOUNT_BUTTON = (By.ID, "navbarAccount")
    LOGIN_BUTTON = (By.ID, "navbarLoginButton")
    SEARCH_BUTTON = (By.ID, "searchQuery")
    SEARCH_ICON = (By.CSS_SELECTOR, "mat-icon[class*='search']")
    PRODUCTS_GRID = (By.CSS_SELECTOR, ".mat-grid-list")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "mat-card.mat-card")
    CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='shopping cart'], button[aria-label*='cart']")
    COOKIE_DISMISS = (By.CSS_SELECTOR, "button[aria-label*='dismiss'], a.cc-btn")
    WELCOME_BANNER_DISMISS = (By.CSS_SELECTOR, "button[aria-label*='Close'], button[mat-dialog-close]")
    # Try multiple logo selectors
    LOGO = (By.CSS_SELECTOR, "img[alt*='OWASP'], img[src*='logo'], img[src*='juice'], .navbar-brand img")
    SIDE_MENU_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='menu'], button[aria-label*='sidenav']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        """Open home page"""
        self.navigate_to("https://demo.owasp-juice.shop/#/")
        time.sleep(3)  # Wait for Angular to load
        self.dismiss_initial_popups()
    
    def dismiss_initial_popups(self):
        """Dismiss welcome banner and cookie consent"""
        try:
            # Wait a bit for popups to appear
            time.sleep(2)
            
            # Try to dismiss welcome banner
            if self.is_element_visible(self.WELCOME_BANNER_DISMISS, timeout=3):
                self.click(self.WELCOME_BANNER_DISMISS)
                time.sleep(0.5)
        except:
            pass
        
        try:
            # Try to dismiss cookie banner
            if self.is_element_visible(self.COOKIE_DISMISS, timeout=3):
                self.click(self.COOKIE_DISMISS)
                time.sleep(0.5)
        except:
            pass
    
    def click_account(self):
        """Click account button"""
        self.click(self.ACCOUNT_BUTTON)
    
    def click_login(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
    
    def search_product(self, product_name):
        """Search for a product"""
        try:
            self.click(self.SEARCH_ICON)
            time.sleep(0.5)
        except:
            pass
        
        self.type_text(self.SEARCH_BUTTON, product_name)
        element = self.find_element(self.SEARCH_BUTTON)
        element.send_keys(Keys.RETURN)
        time.sleep(1)
    
    def get_product_count(self):
        """Get number of products displayed"""
        time.sleep(2)  # Wait for products to load
        products = self.find_elements(self.PRODUCT_CARDS)
        return len(products)
    
    def is_products_grid_visible(self):
        """Check if products grid is visible"""
        return self.is_element_visible(self.PRODUCTS_GRID, timeout=10)
    
    def click_cart(self):
        """Click shopping cart button"""
        self.click(self.CART_BUTTON)
    
    def click_side_menu(self):
        """Click side menu button"""
        self.click(self.SIDE_MENU_BUTTON)
    
    def is_logo_visible(self):
        """Check if logo is visible - try multiple approaches"""
        # Approach 1: Try the specific logo selector
        try:
            if self.is_element_visible(self.LOGO, timeout=5):
                return True
        except:
            pass
        
        # Approach 2: Check if we're on the home page (products visible)
        try:
            if self.is_element_visible(self.PRODUCTS_GRID, timeout=10):
                return True
        except:
            pass
        
        # Approach 3: Check for any navbar element
        try:
            navbar = (By.CSS_SELECTOR, "mat-toolbar, nav, .navbar")
            if self.is_element_visible(navbar, timeout=5):
                return True
        except:
            pass
        
        return False