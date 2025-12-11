"""
Helper utilities for testing
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.core.os_manager import ChromeType
from config.config import Config
from faker import Faker
import time
import platform


fake = Faker()


def get_driver(browser="chrome", headless=False, resolution=None):
    """
    Initialize WebDriver for specified browser
    
    Args:
        browser: Browser name (chrome, firefox, edge)
        headless: Run in headless mode
        resolution: Tuple (width, height) for window size
    
    Returns:
        WebDriver instance
    """
    driver = None
    
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Create ChromeDriverManager with correct architecture
        chrome_driver_manager = ChromeDriverManager()
        
        # Force download of win64 version
        if platform.system() == 'Windows' and platform.machine().endswith('64'):
            import os
            import zipfile
            import requests
            from pathlib import Path
            
            # Get Chrome version
            version = "143.0.7499.42"
            
            # Download URL for win64
            download_url = f"https://storage.googleapis.com/chrome-for-testing-public/{version}/win64/chromedriver-win64.zip"
            
            # Cache directory
            cache_dir = Path.home() / ".wdm" / "drivers" / "chromedriver" / "win64" / version
            cache_dir.mkdir(parents=True, exist_ok=True)
            
            chromedriver_path = cache_dir / "chromedriver-win64" / "chromedriver.exe"
            
            # Download if not exists
            if not chromedriver_path.exists():
                print(f"Downloading ChromeDriver {version} for win64...")
                response = requests.get(download_url)
                zip_path = cache_dir / "chromedriver.zip"
                
                with open(zip_path, 'wb') as f:
                    f.write(response.content)
                
                # Extract
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(cache_dir)
                
                os.remove(zip_path)
                print(f"ChromeDriver installed at: {chromedriver_path}")
            
            driver = webdriver.Chrome(
                service=ChromeService(str(chromedriver_path)),
                options=options
            )
        else:
            # Fallback for other systems
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
    
    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.set_preference("dom.webnotifications.enabled", False)
        
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    
    elif browser.lower() == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-notifications")
        
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
    
    # Set window size
    if resolution:
        driver.set_window_size(resolution[0], resolution[1])
    else:
        driver.maximize_window()
    
    # Set timeouts
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    
    return driver


def generate_random_email():
    """Generate random email address"""
    return fake.email()


def generate_random_password(length=12):
    """Generate random password"""
    return fake.password(length=length, special_chars=True, digits=True, 
                        upper_case=True, lower_case=True)


def generate_test_user():
    """Generate complete test user data"""
    return {
        "email": generate_random_email(),
        "password": generate_random_password(),
        "name": fake.name(),
        "address": fake.address(),
        "phone": fake.phone_number()
    }


def measure_performance(driver, url):
    """
    Measure page load performance
    
    Returns:
        dict with performance metrics
    """
    start_time = time.time()
    driver.get(url)
    load_time = time.time() - start_time
    
    # Get Navigation Timing metrics
    try:
        nav_start = driver.execute_script("return window.performance.timing.navigationStart")
        response_start = driver.execute_script("return window.performance.timing.responseStart")
        dom_complete = driver.execute_script("return window.performance.timing.domComplete")
        load_complete = driver.execute_script("return window.performance.timing.loadEventEnd")
        
        metrics = {
            "total_load_time": load_time,
            "backend_time": (response_start - nav_start) / 1000.0,
            "frontend_time": (dom_complete - response_start) / 1000.0,
            "page_load_time": (load_complete - nav_start) / 1000.0
        }
    except:
        metrics = {"total_load_time": load_time}
    
    return metrics


def take_screenshot(driver, test_name):
    """Take screenshot with timestamp"""
    import os
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(Config.SCREENSHOTS_DIR, filename)
    driver.save_screenshot(filepath)
    return filepath


class BoundaryValues:
    """Boundary value test data generator"""
    
    @staticmethod
    def get_email_boundaries():
        """Get boundary test cases for email"""
        return {
            "valid_min": "a@b.co",
            "valid_normal": "test@example.com",
            "valid_long": "a" * 50 + "@example.com",
            "invalid_no_at": "testexample.com",
            "invalid_no_domain": "test@",
            "invalid_no_local": "@example.com",
            "invalid_spaces": "test @example.com",
            "invalid_special": "test@@example.com"
        }
    
    @staticmethod
    def get_password_boundaries():
        """Get boundary test cases for password"""
        return {
            "valid_min": "Pass1!",
            "valid_normal": "Password123!",
            "valid_long": "P" + "a" * 50 + "1!",
            "invalid_too_short": "Pa1!",
            "invalid_no_number": "Password!",
            "invalid_no_special": "Password123",
            "invalid_no_upper": "password123!",
            "invalid_spaces": "Pass word123!"
        }
    
    @staticmethod
    def get_search_boundaries():
        """Get boundary test cases for search"""
        return {
            "valid_single": "a",
            "valid_normal": "apple",
            "valid_long": "a" * 100,
            "special_chars": "!@#$%",
            "sql_injection": "'; DROP TABLE--",
            "xss_attempt": "<script>alert('xss')</script>",
            "empty": ""
        }