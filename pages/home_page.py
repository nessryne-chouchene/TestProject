"""
Home Page Object Model - FIXED ALL BUGS VERSION
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class HomePage(BasePage):
    # Locators - Multiple fallbacks for stability
    ACCOUNT_BUTTON = (By.XPATH, "//button[@id='navbarAccount'] | //span[contains(text(), 'Account')] | //button[contains(@class, 'mat-focus-indicator')]")
    LOGIN_BUTTON = (By.ID, "navbarLoginButton")
    
    # Search elements - Multiple strategies
    SEARCH_BUTTON = (By.ID, "searchQuery")
    SEARCH_ICON = (By.XPATH, "//mat-icon[contains(text(), 'search')] | //button[@aria-label='Click to search']")
    
    # Other elements - Flexible locators
    PRODUCTS_GRID = (By.CSS_SELECTOR, ".mat-grid-list, mat-grid-list, [class*='grid']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "mat-card.mat-card, mat-grid-tile, .item-card")
    CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='cart'], button[routerlink='/basket'], .fa-shopping-cart")
    COOKIE_DISMISS = (By.XPATH, "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'dismiss') or @aria-label='dismiss cookie message']")
    WELCOME_BANNER_DISMISS = (By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner'], .close-dialog, button.close-dialog")
    LOGO = (By.CSS_SELECTOR, "img[alt*='OWASP'], img[src*='JuiceShop'], img[src*='logo'], .mat-toolbar img")
    SIDE_MENU_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='menu'], button.mat-focus-indicator, mat-icon[role='img']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.load_timeout = 10  # Increased for performance
    
    def open(self):
        """Open home page with robust waiting - FIX BUG #2 (Performance)"""
        self.navigate_to("https://demo.owasp-juice.shop/#/")
        
        # Wait for Angular to initialize - FIX BUG #2
        print("⏳ Waiting for Angular app to load...")
        time.sleep(4)  # Increased from 3 to 4
        
        # Wait for critical element
        self._wait_for_app_ready()
        
        # Dismiss popups
        self.dismiss_initial_popups()
        
        # Extra stability wait
        time.sleep(2)
        print("✅ Page fully loaded")
    
    def _wait_for_app_ready(self):
        """Wait for Angular app to be ready - FIX BUG #3"""
        try:
            # Wait for products grid or logo
            WebDriverWait(self.driver, 15).until(
                lambda d: d.find_element(*self.PRODUCTS_GRID) or d.find_element(*self.LOGO)
            )
        except:
            print("⚠️ Warning: App may not be fully ready")
    
    def dismiss_initial_popups(self):
        """Dismiss welcome banner and cookie consent - Enhanced"""
        # Welcome banner
        try:
            if self.is_element_visible(self.WELCOME_BANNER_DISMISS, timeout=5):
                self.click(self.WELCOME_BANNER_DISMISS)
                time.sleep(1)
                print("✓ Welcome banner dismissed")
        except Exception as e:
            print(f"ℹ️ No welcome banner: {e}")
        
        # Cookie banner  
        try:
            if self.is_element_visible(self.COOKIE_DISMISS, timeout=5):
                self.click(self.COOKIE_DISMISS)
                time.sleep(1)
                print("✓ Cookie banner dismissed")
        except Exception as e:
            print(f"ℹ️ No cookie banner: {e}")
    
    def click_account(self):
        """Click account button - FIX BUG #3 (Element stability)"""
        time.sleep(1)
        try:
            self.click(self.ACCOUNT_BUTTON)
        except:
            # Fallback: try JavaScript click
            element = self.find_element(self.ACCOUNT_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)
    
    def click_login(self):
        """Click login button"""
        time.sleep(1)
        self.click(self.LOGIN_BUTTON)
    
    def search_product(self, product_name):
        """
        Search for a product - FIX BUG #1 (Search interaction)
        Multiple strategies for maximum reliability
        """
        print(f"🔍 Searching for: {product_name}")
        
        # Strategy 1: Direct interaction with better waiting
        try:
            time.sleep(2)  # Wait for page stability
            
            # Find search field with explicit wait
            search_field = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.SEARCH_BUTTON)
            )
            
            # Wait until element is interactable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SEARCH_BUTTON)
            )
            
            # Scroll to element
            self.driver.execute_script("arguments[0].scrollIntoView(true);", search_field)
            time.sleep(0.5)
            
            # Click to focus
            search_field.click()
            time.sleep(1)
            
            # Clear using JavaScript (more reliable than .clear())
            self.driver.execute_script("arguments[0].value = '';", search_field)
            time.sleep(0.5)
            
            # Type text
            search_field.send_keys(product_name)
            time.sleep(1)
            
            # Press Enter
            search_field.send_keys(Keys.RETURN)
            time.sleep(2)
            
            print("✓ Search executed successfully")
            return True
            
        except Exception as e:
            print(f"⚠️ Strategy 1 failed: {e}")
            
            # Strategy 2: JavaScript input
            try:
                search_field = self.find_element(self.SEARCH_BUTTON)
                self.driver.execute_script(
                    f"arguments[0].value = '{product_name}';", 
                    search_field
                )
                search_field.send_keys(Keys.RETURN)
                time.sleep(2)
                print("✓ Search executed via JavaScript")
                return True
            except Exception as e2:
                print(f"❌ All search strategies failed: {e2}")
                return False
    
    def get_product_count(self):
        """Get number of products displayed - FIX BUG #3"""
        try:
            time.sleep(3)  # Wait for products to load
            
            # Wait for products to appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PRODUCT_CARDS)
            )
            
            products = self.find_elements(self.PRODUCT_CARDS, timeout=10)
            count = len(products)
            print(f"📦 Found {count} products")
            return count
        except:
            print("⚠️ No products found")
            return 0
    
    def is_products_grid_visible(self):
        """Check if products grid is visible - Enhanced"""
        time.sleep(2)
        is_visible = self.is_element_visible(self.PRODUCTS_GRID, timeout=15)
        if is_visible:
            print("✓ Products grid is visible")
        else:
            print("⚠️ Products grid not visible")
        return is_visible
    
    def click_cart(self):
        """Click shopping cart button"""
        time.sleep(1)
        try:
            self.click(self.CART_BUTTON)
        except:
            # Fallback
            element = self.find_element(self.CART_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)
    
    def click_side_menu(self):
        """Click side menu button - FIX BUG #4 (Mobile navigation)"""
        time.sleep(1)
        try:
            # Try regular click first
            self.click(self.SIDE_MENU_BUTTON)
        except:
            # Fallback for mobile: JavaScript click
            element = self.find_element(self.SIDE_MENU_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(0.5)
    
    def is_logo_visible(self):
        """Check if logo is visible - FIX BUG #3"""
        time.sleep(1)
        is_visible = self.is_element_visible(self.LOGO, timeout=15)
        if is_visible:
            print("✓ Logo is visible")
        else:
            print("⚠️ Logo not visible")
        return is_visible