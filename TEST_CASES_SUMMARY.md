# Test Cases Summary - 22 Tests Total

## 📋 Overview

| Suite | Test Count | Description |
|-------|-----------|-------------|
| Suite 1: Functional | 10 tests | 5 positive + 5 negative |
| Suite 2: Performance | 4 tests | Load time & stress testing |
| Suite 3: Cross-Browser | 4 tests | Chrome, Firefox, Edge |
| Suite 4: Responsive | 4 tests | Mobile, Tablet, Desktop, Wide |
| **TOTAL** | **22 tests** | ✅ Complete |

---

## 📝 Detailed Test Cases

### **Suite 1: Functional Testing (TC01-TC10)**

#### ✅ Positive Tests (5 tests)

| ID | Test Name | Description | Technique |
|----|-----------|-------------|-----------|
| TC01 | Home page loads successfully | Verify logo and products grid visible | Smoke test |
| TC02 | Search valid product | Search returns results for "apple" | Positive flow |
| TC03 | Navigate to login page | State transition from home to login | State testing |
| TC04 | Cart button accessible | Cart button is visible and clickable | UI validation |
| TC05 | Side menu functionality | Side menu opens on click | UI interaction |

#### ❌ Negative Tests (5 tests)

| ID | Test Name | Description | Technique |
|----|-----------|-------------|-----------|
| TC06 | Login empty email | Login disabled with empty email | Boundary value |
| TC07 | Login invalid email format | Invalid format (no @) rejected | Boundary value |
| TC08 | Search special characters | Search handles !@#$% | Negative testing |
| TC09 | Search SQL injection | SQL injection attempt handled | Security testing |
| TC10 | Search XSS attempt | XSS script tags sanitized | Security testing |

---

### **Suite 2: Performance Testing (TC11-TC14)**

| ID | Test Name | Description | Threshold |
|----|-----------|-------------|-----------|
| TC11 | Home page load time | Measure initial load performance | ≤ 5 seconds |
| TC12 | Search response time | Measure search operation speed | ≤ 3 seconds |
| TC13 | Navigation performance | Measure page transition time | ≤ 3 seconds |
| TC14 | Stress multiple searches | Test 4 consecutive searches | Avg ≤ 3 sec |

**Performance Metrics Tracked:**
- Page load time
- Element response time
- Navigation time
- Average operation time under stress

---

### **Suite 3: Cross-Browser Testing (TC15-TC18)**

**Browsers Tested:** Chrome, Firefox, Edge (3 browsers × 4 tests = 12 executions)

| ID | Test Name | Description |
|----|-----------|-------------|
| TC15 | Home page all browsers | Logo and products visible on all browsers |
| TC16 | Search all browsers | Search functionality works across browsers |
| TC17 | Navigation all browsers | Page navigation works on all browsers |
| TC18 | Cart all browsers | Cart button visible on all browsers |

**Note:** Each test runs on 3 browsers, so 4 test cases × 3 browsers = 12 test executions

---

### **Suite 4: Responsive Design Testing (TC19-TC22)**

**Resolutions Tested:** Mobile (375×667), Tablet (768×1024), Desktop (1920×1080), Wide (2560×1440)

| ID | Test Name | Description |
|----|-----------|-------------|
| TC19 | Responsive home page | Home page displays correctly at all resolutions |
| TC20 | Responsive products grid | Products adapt to screen size |
| TC21 | Responsive navigation | Navigation elements accessible on all sizes |
| TC22 | Responsive search | Search works on all screen sizes |

**Note:** Each test runs on 4 resolutions, so 4 test cases × 4 resolutions = 16 test executions

---

## 🎯 Testing Techniques Applied

### 1. **Boundary Value Testing**
- TC06: Empty email (minimum boundary)
- TC07: Invalid email format (invalid boundary)
- Empty/null inputs tested

### 2. **State Transition Testing**
- TC03: Home → Login navigation
- Page state changes validated

### 3. **Configuration Testing**
- TC15-TC18: Different browsers (Chrome, Firefox, Edge)
- TC19-TC22: Different screen resolutions

### 4. **Performance Testing**
- TC11-TC14: Load times, response times
- Threshold-based validation (5s, 3s)

### 5. **Security Testing**
- TC09: SQL injection attempt
- TC10: XSS (Cross-Site Scripting) attempt

### 6. **Negative Testing**
- TC06-TC10: Invalid inputs, special characters
- Error handling validation

---

## 📊 Test Execution Statistics

### Expected Execution Count

| Suite | Test Cases | Configurations | Total Executions |
|-------|-----------|----------------|------------------|
| Functional | 10 | 1 | 10 |
| Performance | 4 | 1 | 4 |
| Cross-Browser | 4 | 3 browsers | 12 |
| Responsive | 4 | 4 resolutions | 16 |
| **TOTAL** | **22** | **-** | **42 executions** |

---

## 🎓 Test Case Template

Each test follows this structure:

```python
def test_XX_descriptive_name(self):
    """TCXX: Description of what is being tested"""
    
    # 1. Setup/Preconditions
    self.home_page.open()
    
    # 2. Test Actions
    self.home_page.search_product("apple")
    
    # 3. Assertions/Validation
    assert product_count > 0, "Error message"
    
    # 4. Reporting
    print("✓ TCXX PASSED: Description")
```

---

## 🚀 How to Run

### Run All 22 Tests
```bash
pytest tests/ -v --html=reports/all_tests.html --self-contained-html
```

### Run Individual Suites
```bash
pytest tests/test_suite_1_functionality.py -v
pytest tests/test_suite_2_performance.py -v
pytest tests/test_suite_3_cross_browser.py -v
pytest tests/test_suite_4_responsive.py -v
```

### Run Specific Test
```bash
pytest tests/test_suite_1_functionality.py::TestFunctionalSuite::test_01_home_page_loads_successfully -v
```

---

## ✅ Requirements Met

| Requirement | Status | Details |
|-------------|--------|---------|
| Minimum 20 test cases | ✅ YES | 22 test cases |
| 4 test suites | ✅ YES | Functional, Performance, Cross-Browser, Responsive |
| Positive scenarios | ✅ YES | 5 positive tests |
| Negative scenarios | ✅ YES | 5 negative tests |
| Boundary testing | ✅ YES | TC06, TC07 |
| State transitions | ✅ YES | TC03 |
| Configuration testing | ✅ YES | Multiple browsers & resolutions |
| Performance testing | ✅ YES | Suite 2 with thresholds |
| Selenium + Python | ✅ YES | All tests use Selenium |
| ChromeDriver | ✅ YES | Used for Chrome tests |

---

## 📈 Test Coverage

- **Functional Coverage:** Home page, Search, Navigation, Login validation
- **Browser Coverage:** Chrome, Firefox, Edge
- **Device Coverage:** Mobile, Tablet, Desktop, Wide screen
- **Performance Coverage:** Load time, Response time, Stress testing
- **Security Coverage:** SQL injection, XSS attempts

---

**Total Test Cases:** 22 ✅  
**Total Test Executions:** 42 (with browser/resolution variations)  
**Estimated Execution Time:** 15-20 minutes  
**Report Format:** HTML with screenshots