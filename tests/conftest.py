"""
Pytest configuration with automatic bug reporting
"""
import pytest
from datetime import datetime
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.bug_reporter import bug_reporter
from config.config import Config


def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line("markers", "smoke: Mark test as smoke test")
    config.addinivalue_line("markers", "regression: Mark test as regression test")
    config.addinivalue_line("markers", "performance: Mark test as performance test")
    
    print("\n" + "="*60)
    print("🚀 TEST EXECUTION STARTED")
    print("="*60)


def pytest_html_report_title(report):
    """Customize HTML report title"""
    report.title = "OWASP Juice Shop - Test Automation Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture test results and generate bug reports automatically
    This runs after each test
    """
    outcome = yield
    report = outcome.get_result()
    
    # Store report for fixture access
    setattr(item, f"report_{report.when}", report)
    
    # If test failed, log bug automatically
    if report.when == "call" and report.failed:
        test_name = item.nodeid
        error_message = str(report.longrepr)
        
        # Determine severity based on test name or error
        severity = "MEDIUM"
        if "critical" in test_name.lower() or "login" in test_name.lower():
            severity = "HIGH"
        elif "performance" in test_name.lower():
            severity = "HIGH"
        elif "search" in test_name.lower():
            severity = "MEDIUM"
        else:
            severity = "LOW"
        
        # Take screenshot if enabled
        screenshot_path = None
        if Config.AUTO_SCREENSHOT_ON_FAIL and hasattr(item, 'funcargs'):
            if 'driver' in item.funcargs or hasattr(item.instance, 'driver'):
                try:
                    driver = item.funcargs.get('driver') or item.instance.driver
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_name = f"{test_name.replace('::', '_').replace('/', '_')}_{timestamp}.png"
                    screenshot_path = os.path.join(Config.SCREENSHOTS_DIR, screenshot_name)
                    driver.save_screenshot(screenshot_path)
                    print(f"📸 Screenshot saved: {screenshot_path}")
                except Exception as e:
                    print(f"⚠️ Could not take screenshot: {e}")
        
        # Log the bug
        bug_reporter.log_bug(
            test_name=test_name,
            error_message=error_message,
            severity=severity,
            screenshot_path=screenshot_path
        )


def pytest_sessionstart(session):
    """Called before test session starts"""
    print(f"📅 Test Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Reports Dir: {Config.REPORTS_DIR}")
    print(f"🐛 Bugs Dir: {Config.BUGS_DIR}")
    print()


def pytest_sessionfinish(session, exitstatus):
    """Generate bug report after all tests complete"""
    print("\n" + "="*60)
    print("TEST EXECUTION SUMMARY")
    print("="*60)
    print(f"Total tests collected: {session.testscollected}")
    print(f"Exit status: {exitstatus}")
    
    # Generate bug report
    if Config.GENERATE_BUG_REPORT:
        print("\n🐛 Generating bug report...")
        report_path = bug_reporter.generate_report()
        if report_path:
            print(f"✅ Bug report saved to: {report_path}")
        else:
            print("✅ No bugs found - all tests passed!")
    
    print("="*60)


@pytest.fixture(scope="session")
def test_session_data():
    """Store session-wide test data"""
    return {
        "start_time": datetime.now(),
        "test_results": []
    }