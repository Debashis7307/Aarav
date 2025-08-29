#!/usr/bin/env python3
"""
Test script for Murf voice
"""

from speak import speak_text
import time

def test_murf_voice():
    """Test the Murf voice system."""
    print("🎤 Testing Murf Voice...")
    print("=" * 40)
    
    test_messages = [
        "Hello! I'm Aarav, your AI assistant with a beautiful voice powered by Murf!",
        "This is a test of the Murf text-to-speech system.",
        "The voice should sound natural and conversational with the en-US-ken voice.",
        "I can help you with questions, tasks, and conversations!",
        "Thank you for upgrading to Murf voice capabilities!"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n🎵 Test {i}: {message}")
        speak_text(message)
        time.sleep(1)  # Small pause between messages
    
    print("\n✅ Murf voice test completed!")
    print("🎉 Aarav now has a beautiful, conversational voice powered by Murf!")

if __name__ == "__main__":
    test_murf_voice()