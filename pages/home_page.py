"""
Home Page Object Model
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators
    ACCOUNT_BUTTON = (By.ID, "navbarAccount")
    LOGIN_BUTTON = (By.ID, "navbarLoginButton")
    SEARCH_BUTTON = (By.ID, "searchQuery")
    SEARCH_ICON = (By.CSS_SELECTOR, "mat-icon[aria-label='Search']")
    PRODUCTS_GRID = (By.CSS_SELECTOR, ".mat-grid-list")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "mat-card.mat-card")
    CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Show the shopping cart']")
    COOKIE_DISMISS = (By.CSS_SELECTOR, "button[aria-label='dismiss cookie message']")
    WELCOME_BANNER_DISMISS = (By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']")
    LOGO = (By.CSS_SELECTOR, "img[src='assets/public/images/JuiceShop_Logo.png']")
    SIDE_MENU_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Open Sidenav']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        """Open home page"""
        self.navigate_to("https://demo.owasp-juice.shop/#/")
        self.dismiss_initial_popups()
    
    def dismiss_initial_popups(self):
        """Dismiss welcome banner and cookie consent"""
        try:
            # Dismiss welcome banner
            if self.is_element_visible(self.WELCOME_BANNER_DISMISS, timeout=3):
                self.click(self.WELCOME_BANNER_DISMISS)
        except:
            pass
        
        try:
            # Dismiss cookie banner
            if self.is_element_visible(self.COOKIE_DISMISS, timeout=3):
                self.click(self.COOKIE_DISMISS)
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
        self.click(self.SEARCH_ICON)
        self.type_text(self.SEARCH_BUTTON, product_name)
        # Press Enter
        from selenium.webdriver.common.keys import Keys
        element = self.find_element(self.SEARCH_BUTTON)
        element.send_keys(Keys.RETURN)
    
    def get_product_count(self):
        """Get number of products displayed"""
        products = self.find_elements(self.PRODUCT_CARDS)
        return len(products)
    
    def is_products_grid_visible(self):
        """Check if products grid is visible"""
        return self.is_element_visible(self.PRODUCTS_GRID)
    
    def click_cart(self):
        """Click shopping cart button"""
        self.click(self.CART_BUTTON)
    
    def click_side_menu(self):
        """Click side menu button"""
        self.click(self.SIDE_MENU_BUTTON)
    
    def is_logo_visible(self):
        """Check if logo is visible"""
        return self.is_element_visible(self.LOGO)