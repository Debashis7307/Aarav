import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        """Initialize speech recognition."""
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
    
    def listen_and_convert(self):
        """
        Listen to voice input and convert to English text.
        Listens until user stops talking.
        
        Returns:
            str: English text, None if no speech detected
        """
        try:
            with self.microphone as source:
                # Listen without timeout - waits until user stops talking
                audio = self.recognizer.listen(source)
                
                # Convert speech to text (English only)
                text = self.recognizer.recognize_google(audio, language='en-US')
                
                return text
                
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            return None
        except Exception as e:
            return None

# Simple function interface
def listen_to_speech():
    """
    Simple function to listen and convert speech to English text.
    Listens until user stops talking.
    
    Returns:
        str: English text, None if no speech detected
    """
    stt = SpeechToText()
    return stt.listen_and_convert()