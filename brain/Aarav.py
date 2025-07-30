#!/usr/bin/env python3
"""
Aarav AI Assistant - Real-time Conversation
You: Speech to Text → Aarav: Thinking → Aarav: Speaks Response
"""

import sys
import os
sys.path.append('../Communication')

from listen import SpeechToText
from speak import speak_text
from gemini_brain import GeminiBrain
import time
import threading

class Aarav:
    def __init__(self):
        """Initialize Aarav AI Assistant."""
        self.listener = SpeechToText()
        self.brain = GeminiBrain()
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
    
    def is_stop_command(self, text: str) -> bool:
        """Check if the text contains a stop command."""
        text_lower = text.lower().strip()
        return any(stop_cmd in text_lower for stop_cmd in self.stop_commands)
    
    def speak_and_write_word_by_word(self, text: str):
        """Speak and write the text word by word simultaneously."""
        print("🤖 Aarav: ", end="", flush=True)
        
        # Split text into words
        words = text.split()
        
        # Calculate approximate time per word (assuming 150 words per minute)
        words_per_minute = 150
        seconds_per_word = 60 / words_per_minute
        
        # Start speaking in a separate thread
        speak_thread = threading.Thread(target=speak_text, args=(text,))
        speak_thread.start()
        
        # Display words one by one with timing
        for i, word in enumerate(words):
            print(word, end="", flush=True)
            
            # Add space between words (except for the last word)
            if i < len(words) - 1:
                print(" ", end="", flush=True)
            
            # Small delay to match speech timing
            time.sleep(seconds_per_word)
        
        # Wait for speech to complete
        speak_thread.join()
        print()  # New line after completion
    
    def start_conversation(self):
        """Start real-time AI conversation."""
        self.is_running = True
        
        print("🤖 Aarav: yo! I’m Aarav — creative mind, digital soul, curious & clever assistant to Debashis... or as I call him, Devb — my partner in code and chaos!")
        speak_text("yo! I’m Aarav — creative mind, digital soul, curious & clever assistant to Debashis... or as I call him, Devb — my partner in code and chaos!")
        print("🎤 I can help you with questions, tasks, and conversations!")
        speak_text("I can help you with questions, tasks, and conversations!")
        print("🎤 Say 'stop it' or 'bye-bye' to end our conversation.")
        print("🎤 Listening... (Press Ctrl+C to stop)")
        
        while self.is_running:
            try:
                # Step 1: You - Speech to Text
                print("\n🎧 You: ", end="", flush=True)
                user_text = self.listener.listen_and_convert()
                
                if user_text:
                    print(f"[{user_text}]")
                    
                    # Check if it's a stop command
                    if self.is_stop_command(user_text):
                        print("🤖 Aarav: Goodbye! It was great talking with you!")
                        speak_text("Goodbye! It was great talking with you!")
                        self.is_running = False
                        break
                    
                    # Step 2: Aarav - Thinking (Generating Response)
                    print("🧠 Aarav: Thinking...", end="", flush=True)
                    ai_response = self.brain.think(user_text)
                    print(" Done!")
                    
                    # Step 3: Aarav - Speaks and Writes Word by Word
                    self.speak_and_write_word_by_word(ai_response)
                    
                    # Small delay to ensure speech completes
                    time.sleep(0.5)
                else:
                    print("[No speech detected]")
                
            except KeyboardInterrupt:
                print("\n🛑 Stopped by user")
                speak_text("Goodbye! See you next time!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                speak_text("I encountered an error. Let me try again.")
                time.sleep(1)

def main():
    """Main function to run Aarav AI."""
    print("🧠 Aarav AI Assistant")
    print("=" * 40)
    print("Real-time Conversation Flow:")
    print("🎧 You: Speech to Text")
    print("🧠 Aarav: Thinking (Generating)")
    print("🤖 Aarav: Speaks Response")
    print("=" * 40)
    
    # Start Aarav AI
    aarav = Aarav()
    aarav.start_conversation()

if __name__ == "__main__":
    main() 