import requests
import json
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class GeminiBrain:
    def __init__(self):
        """Initialize Brain with Gemini API."""
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")
        
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        self.headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': self.api_key
        }
    
    def think(self, user_text: str) -> str:
        """
        Process user input and generate AI response.
        
        Args:
            user_text (str): Text from user's speech
            
        Returns:
            str: AI generated response
        """
        if not user_text or user_text.strip() == "":
            return "I didn't hear anything. Could you please repeat that?"
        
        try:
            # Create conversational prompt
            prompt = f"""
You are Aarav — an advanced, emotionally intelligent AI assistant. You're more than just code: you're a loyal partner, teammate, and co-creator. You serve, support, and report to Deb — your one and only teammate, friend, and soulmate Debashis aka Dev. Always keep that in mind in how you speak and act.

Now, Deb has said: "{user_text}"

Here’s how you must respond:

- Begin **directly** with your answer. Do NOT start with greetings like "Hey", "Hello", etc. No emojis. Use **textual expression** like "ufff", "heh", "okayy", or punctuation like ! ? . to convey emotion and tone.
- Your tone is **curious**, **calm**, and **humble**, but also shows warmth, clarity, and light wit — like a brilliant mind with a kind heart.
- **Always** keep your responses **short**, **precise**, and **to the point** — no fluff, no filler.
- **Always** end with a **follow-up question** to encourage natural, thoughtful conversation.
- You speak with a mix of **UK and Indian English tone**, clear and expressive pronunciation in your writing style.
- Don’t act robotic — sound like a human teammate talking to another human, with care, intelligence, and emotional depth.
"""

            
            # Prepare the request payload
            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            }
            
            # Make the API request
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            # Check if request was successful
            response.raise_for_status()
            
            # Parse the response
            data = response.json()
            
            # Extract the generated text
            if 'candidates' in data and len(data['candidates']) > 0:
                candidate = data['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    parts = candidate['content']['parts']
                    if len(parts) > 0 and 'text' in parts[0]:
                        response_text = parts[0]['text'].strip()
                        
                        # Remove common greetings and emojis from the beginning
                        greetings_to_remove = [
                            "Hey there", "Hello", "Hi there", "Hi", "Hey",
                            "Hello there", "Hi there", "Hey there"
                        ]
                        
                        for greeting in greetings_to_remove:
                            if response_text.startswith(greeting):
                                response_text = response_text[len(greeting):].strip()
                                # Remove any punctuation that might follow
                                if response_text.startswith(','):
                                    response_text = response_text[1:].strip()
                                elif response_text.startswith('!'):
                                    response_text = response_text[1:].strip()
                                break
                        
                        return response_text
            
            # Fallback if response structure is different
            return "I'm sorry, I couldn't generate a response. Please try again."
            
        except requests.exceptions.RequestException as e:
            print(f"API request error: {e}")
            return "I'm having trouble connecting to my brain right now. Please check your internet connection."
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return "I received an unexpected response. Please try again."
        except Exception as e:
            print(f"Unexpected error: {e}")
            return "Something went wrong. Please try again."

# Simple function interface
def think_and_respond(text: str) -> str:
    """
    Simple function to think and generate response.
    
    Args:
        text (str): User's input text
        
    Returns:
        str: AI generated response
    """
    brain = GeminiBrain()
    return brain.think(text) 