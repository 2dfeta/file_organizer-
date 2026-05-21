#!/usr/bin/env python3
"""
Setup verification script for File Organizer
Checks dependencies, configuration, and creates necessary directories
"""

import os
import sys
import json
from typing import Dict

def check_python_version():
    """Check if Python version is 3.7 or higher."""
    print("🔍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"   ✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor} - requires 3.7 or higher")
        return False

def check_dependencies() -> bool:
    """Check if required packages are installed."""
    print("\n🔍 Checking dependencies...")
    try:
        import schedule  # type: ignore
        print("   ✓ schedule library installed")
        return True
    except ImportError:
        print("   ❌ schedule library not found")
        print("   Install it with: pip install schedule")
        return False

def check_config_file():
    """Check if config.json exists and is valid."""
    print("\n🔍 Checking configuration file...")
    if not os.path.exists("config.json"):
        print("   ❌ config.json not found")
        return False
    
    try:
        with open("config.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
        print("   ✓ config.json is valid JSON")
        
        # Check required keys
        required = ["general", "file_categories", "exclude"]
        for key in required:
            if key not in config:
                print(f"   ⚠️  Missing key: {key}")
                return False
        print("   ✓ All required config keys present")
        return True
    except json.JSONDecodeError as e:
        print(f"   ❌ Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Error reading config: {e}")
        return False

def check_target_directory():
    """Check if target directory exists."""
    print("\n🔍 Checking target directory...")
    try:
        with open("config.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
        target_dir = config["general"]["target_directory"]
        
        if os.path.exists(target_dir):
            print(f"   ✓ Target directory exists: {target_dir}")
            return True
        else:
            print(f"   ⚠️  Target directory not found: {target_dir}")
            print(f"   ℹ️  Please update target_directory in config.json")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def create_logs_directory():
    """Create logs directory if it doesn't exist."""
    print("\n🔧 Setting up directories...")
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        try:
            os.makedirs(logs_dir)
            print(f"   ✓ Created {logs_dir} directory")
        except Exception as e:
            print(f"   ❌ Failed to create logs directory: {e}")
            return False
    else:
        print(f"   ✓ {logs_dir} directory already exists")
    return True

def check_file_permissions():
    """Check if we have write permissions in current directory."""
    print("\n🔍 Checking file permissions...")
    try:
        test_file = ".perm_test"
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        print("   ✓ Write permissions OK")
        return True
    except Exception as e:
        print(f"   ❌ Permission issue: {e}")
        return False

def print_summary(checks: Dict[str, bool]) -> bool:
    """Print summary of all checks."""
    print("\n" + "="*60)
    print("📋 SETUP VERIFICATION SUMMARY")
    print("="*60)
    
    total = len(checks)
    passed = sum(1 for check in checks.values() if check)
    
    print(f"\nPassed: {passed}/{total} checks")
    
    for check_name, result in checks.items():
        status = "✓" if result else "❌"
        print(f"  {status} {check_name}")
    
    print("="*60)
    
    if passed == total:
        print("\n🎉 All checks passed! You're ready to use File Organizer.")
        print("\nNext step: python main.py")
        return True
    else:
        print(f"\n⚠️  {total - passed} check(s) failed. Please resolve the issues above.")
        return False

def main():
    """Run all setup checks."""
    print("\n" + "="*60)
    print("🔧 FILE ORGANIZER - SETUP VERIFICATION")
    print("="*60 + "\n")
    
    checks = {
        "Python Version": check_python_version(),
        "Dependencies": check_dependencies(),
        "Config File": check_config_file(),
        "Target Directory": check_target_directory(),
        "File Permissions": check_file_permissions(),
        "Logs Directory": create_logs_directory(),
    }
    
    success = print_summary(checks)
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
