#!/usr/bin/env python3
"""
Simple test to verify Murf setup
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_murf_setup():
    """Test Murf setup step by step."""
    print("🔧 Testing Murf Setup...")
    print("=" * 40)
    
    # Test 1: Check API key
    api_key = os.getenv('MURF_API_KEY')
    if api_key:
        print(f"✅ API Key found: {api_key[:10]}...")
    else:
        print("❌ MURF_API_KEY not found in environment variables")
        return False
    
    # Test 2: Try to import Murf
    try:
        from murf import Murf
        print("✅ Murf SDK imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Murf SDK: {e}")
        print("💡 Try installing with: pip install murf")
        return False
    
    # Test 3: Try to initialize client with explicit API key
    try:
        client = Murf(api_key=api_key)
        print("✅ Murf client initialized successfully with explicit API key")
    except Exception as e:
        print(f"❌ Failed to initialize Murf client: {e}")
        return False
    
    print("\n🎉 All tests passed! Murf is ready to use.")
    return True

if __name__ == "__main__":
    test_murf_setup()