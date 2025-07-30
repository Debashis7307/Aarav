#!/usr/bin/env python3
"""
Real-time Listen-Speak Integration
You: listen what the user speak
Aarav: convert into text & speak
"""

from listen import SpeechToText
from speak import speak_text
import time

class ListenSpeakSystem:
    def __init__(self):
        """Initialize the listen-speak system."""
        self.listener = SpeechToText()
        self.is_running = False
        
        # Stop commands
        self.stop_commands = [
            "stop it",
            "see you soon", 
            "bye bye",
            "bye-bye",
            "ok bye",
            "ok, bye",
            "goodbye",
            "stop",
            "exit",
            "quit"
        ]
    
    def is_stop_command(self, text):
        """Check if the text contains a stop command."""
        text_lower = text.lower().strip()
        return any(stop_cmd in text_lower for stop_cmd in self.stop_commands)
    
    def start_real_time(self):
        """Start real-time listen and speak system."""
        self.is_running = True
        
        print("🤖 Aarav: Hello! I'm ready to listen and speak.")
        speak_text("Hello! I'm ready to listen and speak.")
        print("🎤 You: Speak anything and I'll repeat it!")
        print("🎤 Listening... (Press Ctrl+C to stop)")
        
        while self.is_running:
            try:
                # Step 1: Listen to user speech
                print("\n🎧 You: ", end="", flush=True)
                text = self.listener.listen_and_convert()
                
                if text:
                    print(f"[{text}]")
                    
                    # Check if it's a stop command
                    if self.is_stop_command(text):
                        print("🤖 Aarav: Goodbye! See you soon!")
                        speak_text("Goodbye! See you soon!")
                        self.is_running = False
                        break
                    
                    # Step 2: Aarav converts to text and speaks
                    print("🤖 Aarav: ", end="", flush=True)
                    speak_text(text)
                    print(f"{text}")
                    
                    # Small delay to ensure speech completes
                    time.sleep(0.5)
                else:
                    print("[No speech detected]")
                
            except KeyboardInterrupt:
                print("\n🛑 Stopped by user")
                speak_text("Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(1)

def main():
    """Main function to run the listen-speak system."""
    system = ListenSpeakSystem()
    system.start_real_time()

if __name__ == "__main__":
    main() 