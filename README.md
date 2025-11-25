# Test Automation Project - OWASP Juice Shop

## 📋 Project Overview

This project implements comprehensive automated testing for the OWASP Juice Shop web application using Selenium WebDriver and Python. It includes 40+ test cases covering functional, performance, cross-browser, and responsive design testing.

**Application Under Test:** https://demo.owasp-juice.shop/

**Testing Framework:** Selenium WebDriver + Pytest

## 🎯 Project Requirements Met

✅ 20+ test cases (40 implemented)  
✅ 4 test suites:
- Suite 1: Functional Testing (21 tests)
- Suite 2: Performance Testing (6 tests)
- Suite 3: Cross-Browser Testing (6 tests)
- Suite 4: Responsive Design Testing (7 tests)

✅ Advanced testing techniques:
- Boundary value testing
- State transition testing
- Configuration testing
- Performance/load testing

✅ Positive and negative test scenarios  
✅ Bug reporting with reproducible steps  
✅ Detailed test execution reports

## 🏗️ Project Structure

```
TestProject/
├── config/
│   └── config.py                 # Configuration settings
├── pages/
│   ├── __init__.py
│   ├── base_page.py             # Base Page Object Model
│   ├── home_page.py             # Home page objects
│   └── login_page.py            # Login page objects
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest configuration
│   ├── test_suite_1_functionality.py
│   ├── test_suite_2_performance.py
│   ├── test_suite_3_cross_browser.py
│   └── test_suite_4_responsive.py
├── utils/
│   ├── __init__.py
│   └── helpers.py               # Helper functions
├── reports/                     # Test reports directory
├── screenshots/                 # Screenshots directory
├── requirements.txt             # Dependencies
├── pytest.ini                   # Pytest configuration
└── README.md                    # This file
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- Mozilla Firefox browser
- Microsoft Edge browser

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd TestProject
```

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

### Run All Test Suites

```bash
pytest tests/ -v --html=reports/full_report.html
```

### Run Specific Test Suite

```bash
# Functional tests
pytest tests/test_suite_1_functionality.py -v

# Performance tests
pytest tests/test_suite_2_performance.py -v

# Cross-browser tests
pytest tests/test_suite_3_cross_browser.py -v

# Responsive tests
pytest tests/test_suite_4_responsive.py -v
```

### Run with Specific Markers

```bash
# Run only smoke tests
pytest -m smoke -v

# Run only performance tests
pytest -m performance -v
```

### Generate HTML Report

```bash
pytest tests/ -v --html=reports/test_report.html --self-contained-html
```

## 📊 Test Cases Overview

### Suite 1: Functional Testing (TC01-TC21)

**Positive Tests:**
- TC01: Home page loads successfully
- TC02: Search for valid product
- TC03: Navigate to login page
- TC04: Login with valid credentials
- TC05: Single character search (boundary)
- TC06: Cart button visibility
- TC07: Side menu opens
- TC08: Products display on load
- TC09: Search with numbers
- TC10: Page title verification

**Negative Tests:**
- TC11: Login with empty email
- TC12: Invalid email format (boundary)
- TC13: Email without domain (boundary)
- TC14: Special characters in search
- TC15: SQL injection attempt (security)
- TC16: XSS attempt (security)
- TC17: Very long search input (boundary)
- TC18: Empty search query (boundary)
- TC19: Email with spaces (boundary)

**State Transition Tests:**
- TC20: Multiple page navigation
- TC21: Cart persistence

### Suite 2: Performance Testing (TC22-TC27)

- TC22: Home page load time measurement
- TC23: Search response time
- TC24: Navigation performance
- TC25: Multiple searches stress test
- TC26: Page reload performance
- TC27: Concurrent element loading

**Performance Thresholds:**
- Max page load time: 5 seconds
- Max element load time: 3 seconds

### Suite 3: Cross-Browser Testing (TC28-TC33)

Tests executed on:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge

**Test Coverage:**
- TC28: Home page loads
- TC29: Search functionality
- TC30: Navigation
- TC31: Cart button visibility
- TC32: Side menu functionality
- TC33: Form validation

### Suite 4: Responsive Design Testing (TC34-TC40)

**Screen Resolutions Tested:**
- Mobile: 375x667 (iPhone SE)
- Tablet: 768x1024 (iPad)
- Desktop: 1920x1080 (Full HD)
- Wide: 2560x1440 (2K)

**Test Coverage:**
- TC34: Home page responsiveness
- TC35: Products grid adaptation
- TC36: Navigation responsiveness
- TC37: Search functionality
- TC38: Cart button visibility
- TC39: Viewport meta tag
- TC40: Mobile menu functionality

## 🐛 Bug Report Template

When bugs are found, they are documented using this structure:

### Bug Report Format

**Bug ID:** BUG-XXX  
**Title:** [Clear, concise description]  
**Severity:** Critical / High / Medium / Low  
**Priority:** P1 / P2 / P3  
**Environment:** Browser, OS, Resolution  
**Test Case:** TC-XX

**Description:**
[Detailed description of the issue]

**Steps to Reproduce:**
1. Step 1
2. Step 2
3. Step 3

**Expected Result:**
[What should happen]

**Actual Result:**
[What actually happens]

**Screenshots/Evidence:**
[Attach screenshots]

**Additional Notes:**
[Any relevant information]

## 📈 Test Results Interpretation

### Pass/Fail Criteria

- **PASSED**: Test executed successfully, assertions met
- **FAILED**: Test failed assertions or encountered errors
- **SKIPPED**: Test was skipped due to conditions
- **ERROR**: Test encountered unexpected error

### Performance Results

Tests include timing measurements:
- Green (✓): Within acceptable threshold
- Red (✗): Exceeds performance threshold

## 🔧 Configuration

Edit `config/config.py` to customize:

```python
# Base URL
BASE_URL = "https://demo.owasp-juice.shop/#/"

# Browser settings
DEFAULT_BROWSER = "chrome"
HEADLESS = False

# Timeouts
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20
PAGE_LOAD_TIMEOUT = 30

# Performance thresholds
MAX_PAGE_LOAD_TIME = 5
MAX_ELEMENT_LOAD_TIME = 3
```

## 📝 Testing Techniques Used

### 1. Boundary Value Testing
- Email validation (min/max length, special chars)
- Password requirements (length, complexity)
- Search input (empty, single char, max length)

### 2. State Transition Testing
- Page navigation flows
- Login/logout states
- Cart state persistence

### 3. Configuration Testing
- Multiple browsers (Chrome, Firefox, Edge)
- Different screen resolutions
- Various environments

### 4. Performance Testing
- Load time measurements
- Response time tracking
- Stress testing with repeated operations

## 🎓 Best Practices Implemented

1. **Page Object Model (POM)**: Separation of page logic and test logic
2. **DRY Principle**: Reusable helper functions and fixtures
3. **Explicit Waits**: Robust element waiting strategies
4. **Error Handling**: Comprehensive try-catch blocks
5. **Logging**: Detailed test execution logs
6. **Screenshots**: Automatic capture on failure
7. **Reporting**: HTML reports with detailed results

## 🤝 Contributing

This is an academic project. For questions or suggestions:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This project is created for educational purposes as part of ISTQB Software Testing certification.

## 👥 Author

[Your Name]  
[Your Email]  
[Date]

## 🙏 Acknowledgments

- OWASP Juice Shop for providing the test application
- Selenium WebDriver community
- Pytest documentation and community

---

**Last Updated:** November 2025