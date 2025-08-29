#!/usr/bin/env python3
"""
Text-to-Speech Module for Aarav AI Assistant

This module supports both Murf and ElevenLabs text-to-speech services.

CURRENTLY ACTIVE: Murf Text-to-Speech
- Voice: en-US-natalie (Inspirational style)
- API Key: MURF_API_KEY (from .env file)
- Previous: en-US-ken (Conversational) - commented out

TO SWITCH TO ELEVENLABS:
1. Uncomment the ElevenLabsSpeaker class (lines ~79-159)
2. Comment out the MurfSpeaker class (lines ~19-77)
3. In get_speaker() function, comment Murf line and uncomment ElevenLabs line
4. Update your .env file with ELEVENLABS_API_KEY

Both implementations are preserved for easy switching.
"""

import os
import tempfile
import time
import requests
from murf import Murf
from dotenv import load_dotenv
import warnings

# Suppress all pygame deprecation warnings
warnings.filterwarnings("ignore", category=UserWarning)

import pygame
import io

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# ACTIVE IMPLEMENTATION: MURF TEXT-TO-SPEECH
# ============================================================================

class MurfSpeaker:
    def __init__(self):
        """Initialize Murf text-to-speech."""
        self.api_key = os.getenv('MURF_API_KEY')
        if not self.api_key:
            raise ValueError("MURF_API_KEY not found in environment variables. Please check your .env file.")
        
        # Initialize Murf client with explicit API key
        self.client = Murf(api_key=self.api_key)
        
        # Initialize pygame mixer for audio playback
        pygame.mixer.init()
        
        # Voice configuration as specified
        # Previous voice (commented out for easy switching):
        # self.voice_id = "en-US-ken"
        # self.style = "Conversational"
        
        # Current active voice:
        self.voice_id = "en-US-natalie"
        self.style = "Inspirational"

    def speak_text(self, text: str):
        """
        Generate and speak text using Murf.
        
        Args:
            text (str): Text to speak
        """
        if not text or text.strip() == "":
            return
            
        try:
            # Generate speech using Murf API
            audio_res = self.client.text_to_speech.generate(
                text=text,
                voice_id=self.voice_id,
                style=self.style
            )
            
            # Get the audio file from response
            audio_file_path = audio_res.audio_file
            
            # Check if it's a URL or file path
            if audio_file_path.startswith('http'):
                # Download the audio file
                import requests
                audio_response = requests.get(audio_file_path)
                audio_data = audio_response.content
            else:
                # Read from local file path
                with open(audio_file_path, 'rb') as audio_file:
                    audio_data = audio_file.read()
            
            # Create a sound object from the audio data
            audio_buffer = io.BytesIO(audio_data)
            sound = pygame.mixer.Sound(audio_buffer)
            
            # Play the sound
            sound.play()
            
            # Wait for the sound to finish playing
            while pygame.mixer.get_busy():
                time.sleep(0.1)
            
        except Exception as e:
            print(f"Murf API error: {e}")
            # Fallback to simple print if speech fails
            print(f"🤖 Aarav: {text}")
    
    def speak(self, text: str):
        """
        Speak the given text (alias for speak_text).
        
        Args:
            text (str): Text to speak
        """
        self.speak_text(text)

# ============================================================================
# COMMENTED IMPLEMENTATION: ELEVENLABS TEXT-TO-SPEECH
# To switch back to ElevenLabs, uncomment this section and comment out Murf section above
# ============================================================================

# class ElevenLabsSpeaker:
#     def __init__(self):
#         """Initialize ElevenLabs text-to-speech."""
#         self.api_key = os.getenv('ELEVENLABS_API_KEY')
#         if not self.api_key:
#             raise ValueError("ELEVENLABS_API_KEY not found in environment variables. Please check your .env file.")
#         
#         self.base_url = "https://api.elevenlabs.io/v1/text-to-speech"
#         self.headers = {
#             'Content-Type': 'application/json',
#             'xi-api-key': self.api_key
#         }
#         
#         # Initialize pygame mixer for audio playback
#         pygame.mixer.init()
#         
#         # Default voice ID (Rachel - a clear, friendly voice)
#         # You can change this to any voice ID from ElevenLabs
#         self.voice_id = "jqcCZkN6Knx8BJ5TBdYR"
#         # Available voices:
#         # jhon-2ro171emrYO7IuOOs8rf, G6TsGA4LBTYQWAMgsYzl|
#         # sam-scOwDtmlUjD3prqpp97I
#         # james-EkK5I93UQWFDigLMpZcX
#         # david-v9LgF91V36LGgbLX3iHW
#         # mask-UgBBYS2sOqTuMpoF3BR0
#         # girl- jqcCZkN6Knx8BJ5TBdYR (aman api) , cgSgspJ2msm6clMCkdW9 , z9fAnlkpzviPz146aGWa (aman api), tnSpp4vdxKPjI9w0GnoV (aman api),  ZF6FPAbjXT4488VcRRnw , 56AoDkrOh6qfVPDXZ7Pt , g6xIsTj2HwM6VR4iXFCw , 0CyqXXfWDNMyXb9GqyLH (aman api)

#     def speak_text(self, text: str):
#         """
#         Generate and speak text using ElevenLabs.
#         
#         Args:
#             text (str): Text to speak
#         """
#         if not text or text.strip() == "":
#             return
#             
#         try:
#             # Prepare the request payload
#             payload = {
#                 "text": text,
#                 "model_id": "eleven_monolingual_v1",
#                 "voice_settings": {
#                     "stability": 0.5,
#                     "similarity_boost": 0.75,
#                     "style": 0.0,
#                     "use_speaker_boost": True
#                 }
#             }
#             
#             # Make the API request
#             url = f"{self.base_url}/{self.voice_id}"
#             response = requests.post(
#                 url,
#                 headers=self.headers,
#                 json=payload,
#                 timeout=30
#             )
#             
#             # Check if request was successful
#             response.raise_for_status()
#             
#             # Get the audio data from response
#             audio_data = response.content
#             
#             # Create a sound object from the audio data
#             audio_file = io.BytesIO(audio_data)
#             sound = pygame.mixer.Sound(audio_file)
#             
#             # Play the sound
#             sound.play()
#             
#             # Wait for the sound to finish playing
#             while pygame.mixer.get_busy():
#                 time.sleep(0.1)
#             
#         except Exception as e:
#             print(f"ElevenLabs API error: {e}")
#             # Fallback to simple print if speech fails
#             print(f"🤖 Aarav: {text}")
#     
#     def speak(self, text: str):
#         """
#         Speak the given text (alias for speak_text).
#         
#         Args:
#             text (str): Text to speak
#         """
#         self.speak_text(text)

# ============================================================================
# GLOBAL FUNCTIONS - CURRENTLY USING MURF
# ============================================================================

# Global speaker instance
_speaker = None

def get_speaker():
    """Get or create the global speaker instance."""
    global _speaker
    if _speaker is None:
        _speaker = MurfSpeaker()  # ACTIVE: Using Murf
        # _speaker = ElevenLabsSpeaker()  # COMMENTED: To use ElevenLabs, uncomment this line and comment above
    return _speaker

def speak_text(text: str):
    """
    Simple function to speak text using Murf.
    
    Args:
        text (str): Text to speak
    """
    speaker = get_speaker()
    speaker.speak_text(text)

# Legacy function for backward compatibility
def speak(text: str):
    """
    Legacy function to speak text (alias for speak_text).
    
    Args:
        text (str): Text to speak
    """
    speak_text(text) 