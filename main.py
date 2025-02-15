import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Print available voices to select one
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.name}")

# Set a different voice (e.g., choose voice 1 if it's available)
engine.setProperty('voice', voices[2].id)  # Change the index to select a different voice

# Speak the text
engine.say("I will speak this text in a different voice.")
engine.runAndWait()
