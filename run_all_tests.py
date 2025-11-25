"""
Script to run all test suites and generate comprehensive reports
"""
import subprocess
import sys
import os
from datetime import datetime


def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")


def run_command(command, description):
    """Run a command and print status"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"❌ {description} failed")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error during {description}: {str(e)}")
        return False


def main():
    """Main execution function"""
    start_time = datetime.now()
    
    print_header("OWASP JUICE SHOP - TEST AUTOMATION EXECUTION")
    print(f"Start Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Create reports directory
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    
    test_suites = [
        {
            "name": "Suite 1: Functional Tests",
            "file": "tests/test_suite_1_functionality.py",
            "report": "reports/suite1_functional.html"
        },
        {
            "name": "Suite 2: Performance Tests",
            "file": "tests/test_suite_2_performance.py",
            "report": "reports/suite2_performance.html"
        },
        {
            "name": "Suite 3: Cross-Browser Tests",
            "file": "tests/test_suite_3_cross_browser.py",
            "report": "reports/suite3_cross_browser.html"
        },
        {
            "name": "Suite 4: Responsive Tests",
            "file": "tests/test_suite_4_responsive.py",
            "report": "reports/suite4_responsive.html"
        }
    ]
    
    results = []
    
    # Run each test suite
    for suite in test_suites:
        print_header(suite["name"])
        command = f'pytest {suite["file"]} -v --html={suite["report"]} --self-contained-html'
        success = run_command(command, suite["name"])
        results.append({"suite": suite["name"], "success": success})
    
    # Run all tests together for consolidated report
    print_header("Generating Consolidated Report")
    command = 'pytest tests/ -v --html=reports/consolidated_report.html --self-contained-html'
    run_command(command, "Consolidated Test Report")
    
    # Print summary
    end_time = datetime.now()
    duration = end_time - start_time
    
    print_header("TEST EXECUTION SUMMARY")
    print(f"End Time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Duration: {duration}")
    print("\nResults:")
    
    for result in results:
        status = "✅ PASSED" if result["success"] else "❌ FAILED"
        print(f"  {status} - {result['suite']}")
    
    print("\n📊 Reports generated in 'reports/' directory:")
    print("  - suite1_functional.html")
    print("  - suite2_performance.html")
    print("  - suite3_cross_browser.html")
    print("  - suite4_responsive.html")
    print("  - consolidated_report.html")
    
    print("\n📸 Screenshots saved in 'screenshots/' directory")
    
    print("\n" + "="*70)
    print("Test execution completed!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()