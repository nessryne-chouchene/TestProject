"""
Test Suite 2: Performance Testing
Contains 4 test cases measuring load times and response times
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
    
    def test_11_home_page_load_time(self):
        """TC11: Measure home page load time"""
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
        print(f"✓ TC11 PASSED: Home page loaded in {load_time:.2f}s")
    
    def test_12_search_response_time(self):
        """TC12: Measure search operation response time"""
        self.home_page.open()
        
        start_time = time.time()
        self.home_page.search_product("apple")
        time.sleep(1)
        response_time = time.time() - start_time
        
        status = "PASS" if response_time <= Config.MAX_ELEMENT_LOAD_TIME else "FAIL"
        self.performance_results.append({
            "test": "Search Response",
            "time": response_time,
            "status": status
        })
        
        assert response_time <= Config.MAX_ELEMENT_LOAD_TIME, \
            f"Search response {response_time:.2f}s too slow"
        print(f"✓ TC12 PASSED: Search completed in {response_time:.2f}s")
    
    def test_13_navigation_performance(self):
        """TC13: Measure navigation between pages"""
        self.home_page.open()
        
        start_time = time.time()
        self.home_page.click_account()
        time.sleep(0.5)
        self.home_page.click_login()
        time.sleep(1)
        nav_time = time.time() - start_time
        
        status = "PASS" if nav_time <= Config.MAX_ELEMENT_LOAD_TIME else "FAIL"
        self.performance_results.append({
            "test": "Navigation Performance",
            "time": nav_time,
            "status": status
        })
        
        assert nav_time <= Config.MAX_ELEMENT_LOAD_TIME, \
            f"Navigation took {nav_time:.2f}s"
        print(f"✓ TC13 PASSED: Navigation completed in {nav_time:.2f}s")
    
    def test_14_stress_multiple_searches(self):
        """TC14: Stress test - Multiple consecutive searches"""
        self.home_page.open()
        search_terms = ["apple", "juice", "banana", "orange"]
        
        total_time = 0
        for term in search_terms:
            start = time.time()
            self.home_page.search_product(term)
            time.sleep(1)
            total_time += time.time() - start
        
        avg_time = total_time / len(search_terms)
        
        status = "PASS" if avg_time <= Config.MAX_ELEMENT_LOAD_TIME else "FAIL"
        self.performance_results.append({
            "test": "Stress Test (avg)",
            "time": avg_time,
            "status": status
        })
        
        assert avg_time <= Config.MAX_ELEMENT_LOAD_TIME, \
            f"Average search time {avg_time:.2f}s too high"
        print(f"✓ TC14 PASSED: Average search time {avg_time:.2f}s for {len(search_terms)} searches")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=reports/performance_tests.html", "--self-contained-html"])