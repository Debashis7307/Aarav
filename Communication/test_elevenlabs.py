#!/usr/bin/env python3
"""
Test script for ElevenLabs voice
"""

from speak import speak_text
import time

def test_elevenlabs_voice():
    """Test the ElevenLabs voice system."""
    print("🎤 Testing ElevenLabs Voice...")
    print("=" * 40)
    
    test_messages = [
        "Hello! I'm Aarav, your AI assistant with a beautiful voice!",
        "This is a test of the ElevenLabs text-to-speech system.",
        "The voice should sound much more natural and human-like than before.",
        "I can help you with questions, tasks, and conversations!",
        "Thank you for upgrading my voice capabilities!"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n🎵 Test {i}: {message}")
        speak_text(message)
        time.sleep(1)  # Small pause between messages
    
    print("\n✅ ElevenLabs voice test completed!")
    print("🎉 Aarav now has a beautiful, human-like voice!")

if __name__ == "__main__":
    test_elevenlabs_voice() 