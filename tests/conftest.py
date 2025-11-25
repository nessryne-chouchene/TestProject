"""
Pytest configuration and fixtures
"""
import pytest
from datetime import datetime
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line("markers", "smoke: Mark test as smoke test")
    config.addinivalue_line("markers", "regression: Mark test as regression test")
    config.addinivalue_line("markers", "performance: Mark test as performance test")


def pytest_html_report_title(report):
    """Customize HTML report title"""
    report.title = "OWASP Juice Shop - Test Automation Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make test result available in fixture"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        setattr(item, f"report_{report.when}", report)


@pytest.fixture(scope="session")
def test_session_data():
    """Store session-wide test data"""
    return {
        "start_time": datetime.now(),
        "test_results": []
    }


def pytest_sessionfinish(session, exitstatus):
    """Print summary after all tests"""
    print("\n" + "="*60)
    print("TEST EXECUTION SUMMARY")
    print("="*60)
    print(f"Total tests run: {session.testscollected}")
    print(f"Exit status: {exitstatus}")
    print("="*60)