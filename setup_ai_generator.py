#!/usr/bin/env python3
"""
AI Test Generator Setup and Configuration
Handles installation, configuration, and provider setup
"""
import os
import sys
import subprocess
import json
from pathlib import Path


class AISetup:
    """Setup and configuration for AI Test Generator"""
    
    def __init__(self):
        self.config_file = Path.home() / ".ai_test_generator.json"
        self.project_root = Path(__file__).parent
        
    def check_dependencies(self):
        """Check if required dependencies are installed"""
        print("🔍 Checking dependencies...")
        
        required_packages = [
            "selenium",
            "webdriver-manager", 
            "faker",
            "requests"
        ]
        
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package)
                print(f"  ✅ {package}")
            except ImportError:
                missing_packages.append(package)
                print(f"  ❌ {package}")
        
        if missing_packages:
            print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
            return self.install_packages(missing_packages)
        else:
            print("✅ All dependencies are installed!")
            return True
    
    def install_packages(self, packages):
        """Install missing packages"""
        try:
            for package in packages:
                print(f"Installing {package}...")
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", package
                ])
            print("✅ All packages installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing packages: {e}")
            return False
    
    def setup_ollama(self):
        """Setup Ollama local AI provider"""
        print("\n🤖 Setting up Ollama (Local AI)...")
        
        # Check if Ollama is installed
        try:
            subprocess.check_call(["ollama", "--version"], 
                                stdout=subprocess.DEVNULL, 
                                stderr=subprocess.DEVNULL)
            print("✅ Ollama is already installed")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("📥 Ollama not found. Installing...")
            
            # Install Ollama based on OS
            if sys.platform.startswith('darwin'):  # macOS
                install_cmd = 'curl -fsSL https://ollama.ai/install.sh | sh'
            elif sys.platform.startswith('linux'):
                install_cmd = 'curl -fsSL https://ollama.ai/install.sh | sh'
            elif sys.platform.startswith('win'):
                print("Please install Ollama manually from: https://ollama.ai")
                return False
            else:
                print("Unsupported OS. Please install Ollama manually.")
                return False
            
            try:
                subprocess.check_call(install_cmd, shell=True)
                print("✅ Ollama installed successfully!")
            except subprocess.CalledProcessError:
                print("❌ Failed to install Ollama")
                return False
        
        # Start Ollama service
        try:
            print("🚀 Starting Ollama service...")
            subprocess.Popen(["ollama", "serve"])
            print("✅ Ollama service started!")
            
            # Pull default model
            print("📥 Downloading default model (this may take a while)...")
            subprocess.check_call(["ollama", "pull", "llama2"])
            print("✅ Model downloaded successfully!")
            
            return True
            
        except subprocess.CalledProcessError:
            print("❌ Failed to start Ollama or download model")
            return False
    
    def setup_huggingface(self):
        """Setup Hugging Face provider"""
        print("\n🤗 Setting up Hugging Face...")
        
        # Install huggingface_hub if not present
        try:
            import huggingface_hub
            print("✅ Hugging Face client already installed")
        except ImportError:
            print("📥 Installing Hugging Face client...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "huggingface_hub"])
                print("✅ Hugging Face client installed!")
            except subprocess.CalledProcessError:
                print("❌ Failed to install Hugging Face client")
                return False
        
        # Check for API token
        token = os.getenv("HUGGINGFACE_API_TOKEN")
        if not token:
            print("\n🔑 Hugging Face API Token Setup:")
            print("1. Go to https://huggingface.co/settings/tokens")
            print("2. Create a new token (read access is sufficient)")
            print("3. Set the environment variable:")
            print("   export HUGGINGFACE_API_TOKEN=your_token_here")
            print("\nFor permanent setup, add to your ~/.bashrc or ~/.zshrc")
        
        return True
    
    def setup_gemini(self):
        """Setup Google Gemini provider"""
        print("\n🌟 Setting up Google Gemini...")
        
        # Install google-generativeai if not present
        try:
            import google.generativeai
            print("✅ Google AI client already installed")
        except ImportError:
            print("📥 Installing Google AI client...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
                print("✅ Google AI client installed!")
            except subprocess.CalledProcessError:
                print("❌ Failed to install Google AI client")
                return False
        
        # Check for API key
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("\n🔑 Google Gemini API Key Setup:")
            print("1. Go to https://makersuite.google.com/app/apikey")
            print("2. Create a new API key")
            print("3. Set the environment variable:")
            print("   export GEMINI_API_KEY=your_api_key_here")
            print("\nFor permanent setup, add to your ~/.bashrc or ~/.zshrc")
        
        return True
    
    def save_config(self, provider_configs):
        """Save configuration to file"""
        config = {
            "providers": provider_configs,
            "default_provider": "ollama",
            "test_suites": {
                "functional": "tests/test_suite_1_functionality.py",
                "performance": "tests/test_suite_2_performance.py",
                "cross_browser": "tests/test_suite_3_cross_browser.py",
                "responsive": "tests/test_suite_4_responsive.py"
            }
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Configuration saved to {self.config_file}")
    
    def load_config(self):
        """Load configuration from file"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {}
    
    def interactive_setup(self):
        """Interactive setup process"""
        print("🚀 AI Test Generator Setup")
        print("=" * 50)
        
        # Check dependencies
        if not self.check_dependencies():
            print("❌ Dependency check failed")
            return False
        
        print("\n📋 Select AI Providers to setup:")
        print("1. Ollama (Local, Free, Recommended)")
        print("2. Hugging Face (Cloud, Free tier)")
        print("3. Google Gemini (Cloud, Free tier)")
        print("4. All of the above")
        
        provider_configs = {}
        
        while True:
            try:
                choice = input("\nEnter choice (1-4): ").strip()
                
                if choice == "1":
                    provider_configs["ollama"] = self.setup_ollama()
                    break
                elif choice == "2":
                    provider_configs["huggingface"] = self.setup_huggingface()
                    break
                elif choice == "3":
                    provider_configs["gemini"] = self.setup_gemini()
                    break
                elif choice == "4":
                    provider_configs["ollama"] = self.setup_ollama()
                    provider_configs["huggingface"] = self.setup_huggingface()
                    provider_configs["gemini"] = self.setup_gemini()
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")
            except KeyboardInterrupt:
                print("\n👋 Setup cancelled!")
                return False
        
        # Save configuration
        self.save_config(provider_configs)
        
        print("\n🎉 Setup completed!")
        print("\nNext steps:")
        print("1. Run tests: python ai_test_cli.py --interactive")
        print("2. Or try: python ai_test_cli.py 'Your user story here' --save")
        print("3. View generated tests in your test files")
        
        return True
    
    def quick_test(self):
        """Run a quick test to verify setup"""
        print("🧪 Running quick test...")
        
        try:
            from utils.ai_test_generator import AITestGenerator, AIProvider
            
            # Test with Ollama (most likely to work locally)
            generator = AITestGenerator(AIProvider.OLLAMA)
            test_cases = generator.generate_from_story(
                "As a user, I want to search for products", 
                "functional"
            )
            
            if test_cases:
                print(f"✅ Generated {len(test_cases)} test cases successfully!")
                return True
            else:
                print("⚠️  No test cases generated. This might be normal if Ollama is not running.")
                return False
                
        except Exception as e:
            print(f"❌ Test failed: {str(e)}")
            return False


def main():
    """Main setup function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="AI Test Generator Setup")
    parser.add_argument("--interactive", "-i", action="store_true", 
                       help="Run interactive setup")
    parser.add_argument("--provider", choices=["ollama", "huggingface", "gemini"],
                       help="Setup specific provider")
    parser.add_argument("--test", action="store_true",
                       help="Run quick test")
    
    args = parser.parse_args()
    
    setup = AISetup()
    
    if args.test:
        setup.quick_test()
    elif args.provider:
        if args.provider == "ollama":
            setup.setup_ollama()
        elif args.provider == "huggingface":
            setup.setup_huggingface()
        elif args.provider == "gemini":
            setup.setup_gemini()
    else:
        setup.interactive_setup()


if __name__ == "__main__":
    main()
