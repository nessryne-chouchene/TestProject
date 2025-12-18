"""
Configuration file for test settings
"""
import os

class Config:
    # Base URL
    BASE_URL = "https://demo.owasp-juice.shop/#/"
    
    # Browser settings
    BROWSERS = ["chrome", "firefox", "edge"]
    DEFAULT_BROWSER = "chrome"
    HEADLESS = False
    
    # Timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30
    
    # Screen resolutions for responsive testing
    RESOLUTIONS = {
        "mobile": (375, 667),      # iPhone SE
        "tablet": (768, 1024),     # iPad
        "desktop": (1920, 1080),   # Full HD
        "wide": (2560, 1440)       # 2K
    }
    
    # Performance thresholds (in seconds)
    MAX_PAGE_LOAD_TIME = 5
    MAX_ELEMENT_LOAD_TIME = 3
    
    # Test data
    VALID_EMAIL = "test@juice-sh.op"
    VALID_PASSWORD = "Test123!"
    
    # Directories
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    REPORTS_DIR = os.path.join(BASE_DIR, "reports")
    SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
    
    # Create directories if they don't exist
    os.makedirs(REPORTS_DIR, exist_ok=True)
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)