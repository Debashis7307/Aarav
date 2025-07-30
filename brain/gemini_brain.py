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
You are Aarav, a helpful and friendly AI assistant. The user said: "{user_text}"

Please provide a helpful, conversational response. Keep it concise but informative. 
Be friendly and natural in your tone, like you're talking to a friend.
IMPORTANT: Do not start with greetings like "Hey there", "Hello", or use emojis. 
Start directly with your response to the user's question or statement.
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