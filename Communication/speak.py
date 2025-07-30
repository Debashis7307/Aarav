import pyttsx3

def speak_text(text):
    """
    Simple function to speak text.
    Creates a fresh engine each time to avoid getting stuck.
    
    Args:
        text (str): Text to speak
    """
    if not text or text.strip() == "":
        return
    
    try:
        # Create a fresh engine each time
        engine = pyttsx3.init()
        
        # Configure voice
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
        
        # Set properties
        engine.setProperty('rate', 150)    # Speed
        engine.setProperty('volume', 0.9)  # Volume
        
        # Speak the text
        engine.say(text)
        engine.runAndWait()
        
        # Clean up
        engine.stop()
        
    except Exception as e:
        print(f"Speech error: {e}")

class SimpleSpeaker:
    def __init__(self):
        """Initialize simple text-to-speech."""
        pass  # No initialization needed
    
    def speak(self, text):
        """
        Speak the given text.
        
        Args:
            text (str): Text to speak
        """
        speak_text(text) 