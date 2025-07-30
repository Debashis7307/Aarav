import os
import tempfile
import time
import requests
from dotenv import load_dotenv
import warnings

# Suppress all pygame deprecation warnings
warnings.filterwarnings("ignore", category=UserWarning)

import pygame
import io

# Load environment variables from .env file
load_dotenv()

class ElevenLabsSpeaker:
    def __init__(self):
        """Initialize ElevenLabs text-to-speech."""
        self.api_key = os.getenv('ELEVENLABS_API_KEY')
        if not self.api_key:
            raise ValueError("ELEVENLABS_API_KEY not found in environment variables. Please check your .env file.")
        
        self.base_url = "https://api.elevenlabs.io/v1/text-to-speech"
        self.headers = {
            'Content-Type': 'application/json',
            'xi-api-key': self.api_key
        }
        
        # Initialize pygame mixer for audio playback
        pygame.mixer.init()
        
        # Default voice ID (Rachel - a clear, friendly voice)
        # You can change this to any voice ID from ElevenLabs
        self.voice_id = "jqcCZkN6Knx8BJ5TBdYR"  
        # Available voices:
   
        # jhon-2ro171emrYO7IuOOs8rf, G6TsGA4LBTYQWAMgsYzl|
        # sam-scOwDtmlUjD3prqpp97I
        # james-EkK5I93UQWFDigLMpZcX
        # david-v9LgF91V36LGgbLX3iHW
        # mask-UgBBYS2sOqTuMpoF3BR0
        # girl- jqcCZkN6Knx8BJ5TBdYR (aman api) , cgSgspJ2msm6clMCkdW9 , z9fAnlkpzviPz146aGWa (aman api), tnSpp4vdxKPjI9w0GnoV (aman api),  ZF6FPAbjXT4488VcRRnw , 56AoDkrOh6qfVPDXZ7Pt , g6xIsTj2HwM6VR4iXFCw , 0CyqXXfWDNMyXb9GqyLH (aman api)

    def speak_text(self, text: str):
        """
        Generate and speak text using ElevenLabs.
        
        Args:
            text (str): Text to speak
        """
        if not text or text.strip() == "":
            return
            
        try:
            # Prepare the request payload
            payload = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                    "style": 0.0,
                    "use_speaker_boost": True
                }
            }
            
            # Make the API request
            url = f"{self.base_url}/{self.voice_id}"
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            # Check if request was successful
            response.raise_for_status()
            
            # Get the audio data from response
            audio_data = response.content
            
            # Create a sound object from the audio data
            audio_file = io.BytesIO(audio_data)
            sound = pygame.mixer.Sound(audio_file)
            
            # Play the sound
            sound.play()
            
            # Wait for the sound to finish playing
            while pygame.mixer.get_busy():
                time.sleep(0.1)
            
        except requests.exceptions.RequestException as e:
            print(f"ElevenLabs API request error: {e}")
            # Fallback to simple print if speech fails
            print(f"🤖 Aarav: {text}")
        except Exception as e:
            print(f"ElevenLabs speech error: {e}")
            # Fallback to simple print if speech fails
            print(f"🤖 Aarav: {text}")
    
    def speak(self, text: str):
        """
        Speak the given text (alias for speak_text).
        
        Args:
            text (str): Text to speak
        """
        self.speak_text(text)

# Global speaker instance
_speaker = None

def get_speaker():
    """Get or create the global speaker instance."""
    global _speaker
    if _speaker is None:
        _speaker = ElevenLabsSpeaker()
    return _speaker

def speak_text(text: str):
    """
    Simple function to speak text using ElevenLabs.
    
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