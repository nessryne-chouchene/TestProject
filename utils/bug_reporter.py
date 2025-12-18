"""
Automatic Bug Reporter
Generates bug reports from test failures
"""
import os
import time
from datetime import datetime
from config.config import Config


class BugReporter:
    """Automatically generates bug reports from test failures"""
    
    def __init__(self):
        self.bugs = []
        self.bug_counter = 1
        self.report_file = os.path.join(
            Config.BUGS_DIR, 
            f"bug_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        )
    
    def log_bug(self, test_name, error_message, severity="MEDIUM", screenshot_path=None):
        """Log a bug found during testing"""
        bug = {
            "id": f"BUG-{self.bug_counter:03d}",
            "test": test_name,
            "severity": severity,
            "error": error_message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "screenshot": screenshot_path
        }
        self.bugs.append(bug)
        self.bug_counter += 1
        print(f"🐛 Bug logged: {bug['id']} - {test_name}")
    
    def generate_report(self):
        """Generate markdown bug report"""
        if not self.bugs:
            print("✅ No bugs found! All tests passed.")
            return None
        
        report = self._generate_markdown()
        
        # Write to file
        with open(self.report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📄 Bug report generated: {self.report_file}")
        return self.report_file
    
    def _generate_markdown(self):
        """Generate markdown formatted report"""
        report = f"""# Automated Bug Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Application:** OWASP Juice Shop  
**Test Framework:** Selenium + Python + Pytest  
**Total Bugs Found:** {len(self.bugs)}

---

## 📊 Summary

| Severity | Count |
|----------|-------|
| HIGH | {sum(1 for b in self.bugs if b['severity'] == 'HIGH')} |
| MEDIUM | {sum(1 for b in self.bugs if b['severity'] == 'MEDIUM')} |
| LOW | {sum(1 for b in self.bugs if b['severity'] == 'LOW')} |

---

"""
        
        # Add each bug
        for bug in self.bugs:
            report += self._format_bug(bug)
        
        return report
    
    def _format_bug(self, bug):
        """Format a single bug entry"""
        severity_emoji = {
            "HIGH": "🔴",
            "MEDIUM": "🟡",
            "LOW": "🟢"
        }
        
        emoji = severity_emoji.get(bug['severity'], "⚪")
        
        bug_entry = f"""
## {emoji} {bug['id']}: {bug['test']}

**Severity:** {bug['severity']}  
**Found:** {bug['timestamp']}  
**Test Case:** {bug['test']}

### Error Details
```
{bug['error']}
```

### Steps to Reproduce
1. Run test: `pytest {bug['test']} -v`
2. Observe the failure
3. Check error message above

### Expected Result
Test should pass without errors

### Actual Result
Test failed with error shown above

"""
        
        if bug['screenshot']:
            bug_entry += f"""### Screenshot
![Bug Screenshot]({bug['screenshot']})

"""
        
        bug_entry += "---\n\n"
        
        return bug_entry


# Global bug reporter instance
bug_reporter = BugReporter()