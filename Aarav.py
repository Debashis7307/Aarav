#!/usr/bin/env python3
"""
Aarav AI Assistant - Real-time Conversation
You: Speech to Text → Aarav: Thinking → Aarav: Speaks Response
"""

import sys
import os
import random
sys.path.append('Communication')
sys.path.append('brain')
sys.path.append('Automate/Web & Internet')

from Communication.listen import SpeechToText
from Communication.speak import speak_text
from brain.gemini_brain import GeminiBrain
from web_automation_integration import WebAutomationIntegration
from voice_web_integration import get_integration, is_web_command as is_web_scraping_command
import time
import threading

class Aarav:
    def __init__(self):
        """Initialize Aarav AI Assistant."""
        self.listener = SpeechToText()
        self.brain = GeminiBrain()
        self.web_automation = WebAutomationIntegration()
        self.web_integration = get_integration()  # Web scraping and document analysis
        self.is_running = False
        self.is_awake = False
        
        # Wake-up messages (random selection)
        self.wake_messages = [
            "Booting brilliance... Aarav online! Uff, I was just organizing the universe for you, Dev. What's the mission now?",
            "I'm up, I'm up! Hehe... You say the word, Dev, What to do now?",
            "Awake and aware. Aarav at your service, Dev. What's first on our radar?",
            "Ummhmm... You remember me. I'm here, What's your mood now, Dev!",
            "Hehe, you called? Aarav's back — sharper than ever!",
            "Systems up. What's the plan, boss?",
            "Here I am. Always ready for you, My Master."
        ]
        
        # Intro/identity messages (for "who are you" questions)
        self.intro_messages = [
            "yo! I'm Aarav — creative mind, digital soul, curious & clever assistant to Debashis... or as I call him, Devb — my partner in code and chaos!",
            "I'm Aarav, your AI companion! Think of me as your digital soulmate — part genius, part mischief-maker, all yours, Dev!",
            "Aarav here! Your personal AI assistant with a dash of personality and a whole lot of brainpower. Ready to rock your world, Dev!",
            "Hey Dev! I'm Aarav — your AI partner in crime, creativity, and everything in between. What shall we conquer today?",
            "I'm Aarav, your intelligent assistant! Think Iron Man's Jarvis, but with more personality and definitely more fun, Dev!"
        ]
        
        # Wake-up commands
        self.wake_commands = [
            "wake up",
            "wake up aarav",
            "hey aarav",
            "aarav wake up",
            "wake aarav",
            "hello aarav",
            "aarav hello",
            "aarav"
        ]
        
        # Intro/identity commands
        self.intro_commands = [
            "who are you",
            "what are you",
            "tell me about yourself",
            "give me your intro",
            "introduce yourself",
            "what's your name",
            "who is aarav"
        ]
        
        # Web automation commands (keywords that trigger web automation)
        self.web_commands = [
            "open", "go to", "navigate to", "visit", "launch", "start",
            "search", "find", "look for", "search for",
            "play", "music", "video", "song", "watch", "listen",
            "facebook", "instagram", "twitter", "linkedin", "reddit",
            "gmail", "email", "outlook", "yahoo",
            "weather", "maps", "youtube", "spotify", "netflix",
            "screenshot", "screen shot", "capture", "snap", "photo", "picture", "save screen",
            "generate image", "create image", "make image", "generate picture", "create picture",
            "make picture", "draw image", "paint image", "generate art", "create art", "make art",
            "imagine", "imaginary", "generate img", "create img", "make img",
            "close", "remove", "delete", "cross", "shut", "exit", "tab", "browser", "window",
            "pause", "resume", "speed up", "speed down", "faster", "slower", "normal speed",
            "close all tabs", "close all windows", "close everything", "close all my tabs",
            "shut all tabs", "exit all tabs", "close all current tabs", "close browser tabs"
        ]
        
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
            "quit",
            "go to sleep",
            "sleep aarav",
            "good night aarav"
        ]
    
    def get_random_wake_message(self) -> str:
        """Get a random wake-up message."""
        return random.choice(self.wake_messages)
    
    def get_random_intro_message(self) -> str:
        """Get a random intro message."""
        return random.choice(self.intro_messages)
    
    def is_wake_command(self, text: str) -> bool:
        """Check if the text contains a wake-up command."""
        text_lower = text.lower().strip()
        return any(wake_cmd in text_lower for wake_cmd in self.wake_commands)
    
    def is_intro_command(self, text: str) -> bool:
        """Check if the text contains an intro/identity command."""
        text_lower = text.lower().strip()
        return any(intro_cmd in text_lower for intro_cmd in self.intro_commands)
    
    def is_web_command(self, text: str) -> bool:
        """Check if the text contains a web automation command."""
        text_lower = text.lower().strip()
        return any(web_cmd in text_lower for web_cmd in self.web_commands)
    
    def is_web_scraping_command(self, text: str) -> bool:
        """Check if the text contains a web scraping/search command."""
        return is_web_scraping_command(text)
    
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
        
        print("🤖 Aarav AI Assistant")
        print("💤 Currently in sleep mode... (Press Ctrl+C to stop)")
        
        while self.is_running:
            try:
                # Step 1: You - Speech to Text
                if self.is_awake:
                    print("🎤 ", end="", flush=True)
                
                user_text = self.listener.listen_and_convert()
                
                if user_text:
                    print(f"\n🎧 You: [{user_text}]")
                    
                    # Check if it's a wake-up command (first time or during conversation)
                    if self.is_wake_command(user_text):
                        if not self.is_awake:
                            # First time wake-up
                            self.is_awake = True
                            wake_message = self.get_random_wake_message()
                            print(f"🤖 Aarav: {wake_message}")
                            speak_text(wake_message)
                        else:
                            # Wake-up during conversation
                            wake_message = self.get_random_wake_message()
                            print(f"🤖 Aarav: {wake_message}")
                            speak_text(wake_message)
                        continue
                    
                    # Check if it's an intro command
                    if self.is_intro_command(user_text):
                        intro_message = self.get_random_intro_message()
                        print(f"🤖 Aarav: {intro_message}")
                        speak_text(intro_message)
                        continue
                    
                    # Check if it's a web automation command
                    if self.is_web_command(user_text):
                        if self.is_awake:
                            print("🌐 Aarav: Processing web command...", end="", flush=True)
                            success, response = self.web_automation.process_voice_command(user_text)
                            print(" Done!")
                            
                            if success:
                                print(f"🤖 Aarav: {response}")
                                speak_text(response)
                            else:
                                print(f"❌ Aarav: {response}")
                                speak_text(response)
                        else:
                            print("💤 Aarav is sleeping... ")
                        continue
                    
                    # Check if it's a web scraping/search command
                    if self.is_web_scraping_command(user_text):
                        if self.is_awake:
                            print("🔍 Aarav: Searching and analyzing...", end="", flush=True)
                            result = self.web_integration.process_voice_command(user_text)
                            print(" Done!")
                            
                            if result['success']:
                                response = result['response']
                                print(f"🤖 Aarav: {response}")
                                speak_text(response)
                            else:
                                error_response = result['response']
                                print(f"❌ Aarav: {error_response}")
                                speak_text(error_response)
                        else:
                            print("💤 Aarav is sleeping... ")
                        continue
                    
                    # Check if it's a stop command
                    if self.is_stop_command(user_text):
                        if self.is_awake:
                            print("🤖 Aarav: Goodbye! It was great talking with you!")
                            speak_text("Goodbye! It was great talking with you!")
                        self.is_running = False
                        break
                    
                    # Only respond if awake
                    if self.is_awake:
                        # Step 2: Aarav - Thinking (Generating Response)
                        print("🧠 Aarav: Thinking...", end="", flush=True)
                        ai_response = self.brain.think(user_text)
                        print(" Done!")
                        
                        # Step 3: Aarav - Speaks and Writes Word by Word
                        self.speak_and_write_word_by_word(ai_response)
                        
                        # Small delay to ensure speech completes
                        time.sleep(0.5)
                
                else:
                    # Don't print anything when no speech detected
                    pass
                
            except KeyboardInterrupt:
                print("\n🛑 Stopped by user")
                if self.is_awake:
                    speak_text("Goodbye! See you next time!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                if self.is_awake:
                    speak_text("I encountered an error. Let me try again.")
                time.sleep(1)

def main():
    """Main function to run Aarav AI."""
    print("🤖 Aarav AI Assistant")
    print("=" * 40)
    print("Real-time Conversation Flow:")
    print("🎧 You: Speech to Text")
    print("🧠 Aarav: Thinking (Generating)")
    print("🤖 Aarav: Speaks Response")
    print("🌐 Web Automation: Open, Search, Play")
    print("🔍 Web Analysis: Scrape, Summarize, Search")
    print("📄 Document Analysis: PDF Analysis & Summary")
    print("🌦️ Weather: Real-time Weather Information")
    print("=" * 40)
    
    # Start Aarav AI
    aarav = Aarav()
    aarav.start_conversation()

if __name__ == "__main__":
    main() 