# AI-Powered Test Case Generator

A completely free AI-powered test case generator that automatically creates comprehensive test cases from user stories. No payment required - uses free AI APIs to generate tests that integrate seamlessly with your existing pytest + Selenium test framework.

## 🚀 Features

- **100% Free**: Uses free AI APIs (Ollama local, Hugging Face, Google Gemini)
- **Automatic Test Generation**: Converts user stories into comprehensive test cases
- **Multiple Test Types**: Generates positive, negative, boundary, performance, and security tests
- **Seamless Integration**: Automatically adds tests to your existing test suite files
- **Interactive Mode**: Easy-to-use guided interface
- **Multiple AI Providers**: Choose from local (Ollama) or cloud-based free options

## 📋 Prerequisites

- Python 3.7+
- pip (Python package manager)
- Chrome browser (for Selenium tests)
- Internet connection (for cloud AI providers)

## 🛠️ Quick Setup

### 1. Run Setup (One-time)

```bash
python setup_ai_generator.py --interactive
```

This will:
- Check and install required dependencies
- Set up AI providers (Ollama recommended for local use)
- Configure everything automatically

### 2. Generate Tests

#### Interactive Mode (Recommended for beginners)
```bash
python ai_test_cli.py --interactive
```

#### Command Line Mode
```bash
# Generate functional tests
python ai_test_cli.py "As a user, I want to search for products and add them to cart" --save

# Generate performance tests  
python ai_test_cli.py "As a user, I want fast page loading" --suite performance --save

# Use specific AI provider
python ai_test_cli.py "As a user, I want to reset my password" --provider ollama --save
```

## 🎯 How It Works

1. **User Story Input**: You provide a user story describing functionality to test
2. **AI Analysis**: Free AI analyzes your story and understands context
3. **Test Generation**: AI generates comprehensive test cases including:
   - Positive test cases (happy path)
   - Negative test cases (error conditions)
   - Boundary value tests (edge cases)
   - Performance tests (if applicable)
   - Security tests (if applicable)
4. **Automatic Integration**: Tests are automatically added to your test suite files

## 📖 Usage Examples

### Example 1: Shopping Cart Functionality

**User Story**: "As a customer, I want to add products to my shopping cart so I can purchase them later"

**Generated Tests** (automatically added to `test_suite_1_functionality.py`):
```python
def test_01_add_single_product_to_cart(self):
    """TC01: Verify single product can be added to cart"""
    self.home_page.open()
    self.home_page.search_product("apple")
    time.sleep(1)
    
    # Add first product to cart
    self.home_page.click_add_to_cart_button()
    time.sleep(1)
    
    # Verify cart count increased
    cart_count = self.home_page.get_cart_count()
    assert cart_count > 0, "Product not added to cart"
    print("✓ TC01 PASSED: Single product added to cart")

def test_02_add_multiple_products_to_cart(self):
    """TC02: Verify multiple products can be added to cart"""
    # ... comprehensive test code generated
```

### Example 2: User Registration

**User Story**: "As a new user, I want to create an account so I can save my preferences"

**Generated Tests** (added to test suite):
```python
def test_03_registration_with_valid_data(self):
    """TC03: Verify user registration with valid data"""
    # ... test implementation
```

## 🔧 AI Provider Options

### 1. Ollama (Recommended - Local & Free)
- **Cost**: Completely free
- **Setup**: Local installation required
- **Pros**: Privacy, no internet required after setup, no usage limits
- **Cons**: Requires initial setup and model download

**Setup**:
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start service and download model
ollama serve
ollama pull llama2
```

### 2. Hugging Face (Cloud - Free Tier)
- **Cost**: Free tier available
- **Setup**: API token required
- **Pros**: No local installation, good model variety
- **Cons**: Requires internet, usage limits on free tier

**Setup**:
```bash
# Get token from https://huggingface.co/settings/tokens
export HUGGINGFACE_API_TOKEN=your_token_here
```

### 3. Google Gemini (Cloud - Free Tier)
- **Cost**: Free tier available
- **Setup**: API key required
- **Pros**: Powerful model, no local setup
- **Cons**: Requires internet, usage limits

**Setup**:
```bash
# Get API key from https://makersuite.google.com/app/apikey
export GEMINI_API_KEY=your_api_key_here
```

## 📁 Project Structure

After generation, your tests will be organized as follows:

```
tests/
├── test_suite_1_functionality.py    # Functional tests (UI interactions)
├── test_suite_2_performance.py      # Performance tests (load times)
├── test_suite_3_cross_browser.py    # Cross-browser tests
├── test_suite_4_responsive.py       # Responsive design tests
└── generated/                       # AI-generated tests
    ├── additional_functional_tests.py
    └── security_tests.py
```

## 🧪 Test Generation Types

### Functional Tests
- User interactions (clicking, typing)
- Form submissions
- Navigation flows
- Data validation

### Performance Tests
- Page load times
- Response times
- Memory usage
- Concurrent user handling

### Cross-Browser Tests
- Browser compatibility
- Feature consistency
- Rendering differences

### Responsive Tests
- Mobile/tablet/desktop layouts
- Touch interactions
- Screen size adaptations

### Security Tests
- Input validation
- SQL injection attempts
- XSS protection
- Authentication bypasses

## 🔍 Generated Test Structure

Each generated test follows this pattern:

```python
def test_descriptive_name(self):
    """TC##: Brief description of what is tested"""
    # Setup
    self.home_page.open()
    
    # Action
    # ... specific test steps ...
    
    # Assertion
    assert expected_result, "Failure message"
    print("✓ TC## PASSED: Test description")
```

## 🚦 Running Generated Tests

After generating tests, run them using your existing test runner:

```bash
# Run all tests
python run_all_tests.py

# Run specific test suite
pytest tests/test_suite_1_functionality.py -v

# Run with HTML reports
pytest tests/ -v --html=reports/report.html --self-contained-html
```

## 🎛️ Advanced Usage

### Custom Output File
```bash
python ai_test_cli.py "Your user story" --output custom_tests.py
```

### Generate Without Saving (Preview Only)
```bash
python ai_test_cli.py "Your user story" --preview
```

### Batch Generation
```bash
# Create a file with multiple user stories
echo "As a user, I want to search products
As a user, I want to checkout
As a user, I want to manage profile" > stories.txt

# Generate for each story
while read story; do
    python ai_test_cli.py "$story" --save
done < stories.txt
```

## 🔧 Configuration

The AI generator automatically creates configuration in `~/.ai_test_generator.json`:

```json
{
  "providers": {
    "ollama": true,
    "huggingface": false,
    "gemini": false
  },
  "default_provider": "ollama",
  "test_suites": {
    "functional": "tests/test_suite_1_functionality.py",
    "performance": "tests/test_suite_2_performance.py",
    "cross_browser": "tests/test_suite_3_cross_browser.py",
    "responsive": "tests/test_suite_4_responsive.py"
  }
}
```

## 🐛 Troubleshooting

### Common Issues

**1. "Ollama is not running"**
```bash
# Start Ollama service
ollama serve

# In another terminal, pull model
ollama pull llama2
```

**2. "No test cases generated"**
- Check if AI provider is properly set up
- Try with different user story (more specific)
- Check internet connection for cloud providers

**3. "Permission denied"**
```bash
chmod +x ai_test_cli.py
chmod +x setup_ai_generator.py
```

**4. "Module not found"**
```bash
# Install missing dependencies
pip install selenium webdriver-manager faker requests huggingface_hub google-generativeai
```

### Getting Help

1. Run setup again: `python setup_ai_generator.py --interactive`
2. Check logs for specific error messages
3. Try different AI providers
4. Verify your user story is descriptive enough

## 💡 Tips for Better Test Generation

1. **Be Specific**: "As a user, I want to filter products by price range" works better than "I want to filter"

2. **Include Context**: Mention the application type (e-commerce, banking, etc.)

3. **Specify Test Type**: Use `--suite performance` for performance-related stories

4. **Review Generated Tests**: Always review and customize generated tests for your specific needs

5. **Iterate**: Generate multiple test variations and combine the best parts

## 🎯 Example User Stories That Work Well

**Good Examples**:
- "As a customer, I want to search for products by category and price range"
- "As a registered user, I want to update my profile information"
- "As a shopper, I want to apply discount coupons during checkout"
- "As a mobile user, I want the interface to work well on my phone"

**Too Vague**:
- "I want to test search" (instead: "As a user, I want to search for products by name")

## 🔄 Integration with CI/CD

Add to your CI pipeline:

```yaml
# .github/workflows/test.yml
- name: Generate AI Tests
  run: |
    python ai_test_cli.py "As a user, I want to test new feature" --save

- name: Run Tests
  run: |
    python run_all_tests.py
```

## 📈 Benefits

- **Time Savings**: Generate comprehensive test suites in minutes instead of hours
- **Coverage**: AI thinks of edge cases you might miss
- **Consistency**: Generated tests follow your established patterns
- **Free**: No ongoing costs or API usage fees
- **Learning**: See how AI approaches test design

## 🚀 Next Steps

1. **Setup**: Run the interactive setup
2. **Generate**: Try with a simple user story
3. **Customize**: Modify generated tests to match your specific needs
4. **Integrate**: Add to your CI/CD pipeline
5. **Scale**: Generate tests for all your user stories

---

**Ready to get started?** Run: `python setup_ai_generator.py --interactive`
