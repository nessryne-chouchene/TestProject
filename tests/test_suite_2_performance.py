"""
Test Suite 2: Performance Testing
Measures page load times, response times, and stress testing
"""
import pytest
import time
from pages.home_page import HomePage
from utils.helpers import get_driver, measure_performance
from config.config import Config


class TestPerformanceSuite:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup before each test"""
        self.driver = get_driver("chrome")
        self.home_page = HomePage(self.driver)
        self.performance_results = []
        yield
        self.driver.quit()
        
        # Print performance summary
        if self.performance_results:
            print("\n" + "="*50)
            print("PERFORMANCE TEST SUMMARY")
            print("="*50)
            for result in self.performance_results:
                print(f"{result['test']}: {result['time']:.2f}s - {result['status']}")
            print("="*50)
    
    def test_22_home_page_load_time(self):
        """TC22: Measure home page load time"""
        url = Config.BASE_URL
        metrics = measure_performance(self.driver, url)
        load_time = metrics.get("page_load_time", metrics["total_load_time"])
        
        status = "PASS" if load_time <= Config.MAX_PAGE_LOAD_TIME else "FAIL"
        self.performance_results.append({
            "test": "Home Page Load",
            "time": load_time,
            "status": status
        })
        
        assert load_time <= Config.MAX_PAGE_LOAD_TIME, \
            f"Page load time {load_time:.2f}s exceeds threshold {Config.MAX_PAGE_LOAD_TIME}s"
        print(f"✓ TC22 PASSED: Home page loaded in {load_time:.2f}s")
    
    def test_23_search_response_time(self):
        """TC23: Measure search operation response time"""
        self.home_page.open()
        
        start_time = time.time()
        self.home_page.search_product("apple")
        time.sleep(1)  # Wait for results to load
        response_time = time.time() - start_time
        
        status = "PASS" if response_time <= Config.MAX_ELEMENT_LOAD_TIME else "FAIL"
        self.performance_results.append({
            "test": "Search Response",
            "time": response_time,
            "status": status
        })
        
        assert response_time <= Config.MAX_ELEMENT_LOAD_TIME, \
            f"Search response {response_time:.2f}s too slow"
        print(f"✓ TC23 PASSED: Search completed in {response_time:.2f}s")
    
    def test_24_navigation_performance(self):
        """TC24: Measure navigation between pages"""
        self.home_page.open()
        
        start_time = time.time()
        self.home_page.click_account()
        time.sleep(0.5)
        self.home_page.click_login()
        time.sleep(1)
        nav_time = time.time() - start_time
        
        status = "PASS" if nav_time <= Config.MAX_ELEMENT_LOAD_TIME else "FAIL"
        self.performance_results.append({
            "test": "Navigation to Login",
            "time": nav_time,
            "status": status
        })
        
        assert nav_time <= Config.MAX_ELEMENT_LOAD_TIME, \
            f"Navigation took {nav_time:.2f}s"
        print(f"✓ TC24 PASSED: Navigation completed in {nav_time:.2f}s")
    
    def test_25_multiple_searches_performance(self):
        """TC25: Stress test - Multiple consecutive searches"""
        self.home_page.open()
        search_terms = ["apple", "juice", "banana", "orange", "lemon"]
        
        total_time = 0
        for term in search_terms:
            start = time.time()
            self.home_page.search_product(term)
            time.sleep(1)
            total_time += time.time() - start
        
        avg_time = total_time / len(search_terms)
        
        status = "PASS" if avg_time <= Config.MAX_ELEMENT_LOAD_TIME else "FAIL"
        self.performance_results.append({
            "test": "Multiple Searches (avg)",
            "time": avg_time,
            "status": status
        })
        
        assert avg_time <= Config.MAX_ELEMENT_LOAD_TIME, \
            f"Average search time {avg_time:.2f}s too high"
        print(f"✓ TC25 PASSED: Average search time {avg_time:.2f}s")
    
    def test_26_page_reload_performance(self):
        """TC26: Measure page reload performance"""
        self.home_page.open()
        time.sleep(2)  # Let initial load complete
        
        start_time = time.time()
        self.driver.refresh()
        time.sleep(2)  # Wait for reload
        reload_time = time.time() - start_time
        
        status = "PASS" if reload_time <= Config.MAX_PAGE_LOAD_TIME else "FAIL"
        self.performance_results.append({
            "test": "Page Reload",
            "time": reload_time,
            "status": status
        })
        
        assert reload_time <= Config.MAX_PAGE_LOAD_TIME
        print(f"✓ TC26 PASSED: Page reloaded in {reload_time:.2f}s")
    
    def test_27_concurrent_element_loading(self):
        """TC27: Test loading time with multiple elements"""
        self.home_page.open()
        
        start_time = time.time()
        # Wait for all products to load
        time.sleep(2)
        product_count = self.home_page.get_product_count()
        load_time = time.time() - start_time
        
        status = "PASS" if load_time <= Config.MAX_PAGE_LOAD_TIME else "FAIL"
        self.performance_results.append({
            "test": f"Load {product_count} Products",
            "time": load_time,
            "status": status
        })
        
        assert product_count > 0, "No products loaded"
        assert load_time <= Config.MAX_PAGE_LOAD_TIME
        print(f"✓ TC27 PASSED: {product_count} products loaded in {load_time:.2f}s")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=reports/performance_tests.html"])