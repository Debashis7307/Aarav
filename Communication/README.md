# 🎤 Voice Listening Module

This module provides voice recognition capabilities for your AI assistant, supporting both English and Hindi speech input.

## 📁 Files

- **`listen.py`** - Full version with translation capabilities
- **`listen_simple.py`** - Simplified version without external translation
- **`requirements.txt`** - Required dependencies

## 🚀 Quick Start

### Install Dependencies

```bash
pip install -r Communication/requirements.txt
```

### Basic Usage

```python
from Communication.listen_simple import SimpleVoiceListener

# Create listener
listener = SimpleVoiceListener()

# Listen once
text, language = listener.listen_once()
print(f"You said: {text} in {language}")

# Listen continuously
def on_speech(text, language):
    print(f"Processed: {text} ({language})")

listener.listen_continuous(on_speech)
```

## 🎯 Features

### SimpleVoiceListener (`listen_simple.py`)

- ✅ Speech recognition (English + Hindi)
- ✅ Language detection
- ✅ Continuous listening
- ✅ Text-to-speech response
- ✅ No external dependencies for translation

### VoiceListener (`listen.py`)

- ✅ All features from SimpleVoiceListener
- ✅ Hindi to English translation (requires googletrans)
- ✅ More advanced language processing

## 🔧 Usage Examples

### Single Voice Input

```python
from Communication.listen_simple import SimpleVoiceListener

listener = SimpleVoiceListener()
text, lang = listener.listen_once(timeout=10)

if text:
    print(f"Detected: {text} ({lang})")
else:
    print("No speech detected")
```

### Continuous Listening (Jarvis-style)

```python
from Communication.listen_simple import SimpleVoiceListener

listener = SimpleVoiceListener()

def process_speech(text, language):
    print(f"🎧 You said: {text}")
    print(f"🌍 Language: {language}")

    # Add your AI processing here
    if "hello" in text.lower():
        listener.speak("Hello! How can I help you?")
    elif "stop" in text.lower():
        listener.stop_listening()

# Start continuous listening
thread = listener.listen_continuous(process_speech)

# Keep the program running
try:
    thread.join()
except KeyboardInterrupt:
    listener.stop_listening()
```

## 🎮 Test the Module

### Test Basic Functionality

```bash
python test_listen.py
```

### Test Voice Recognition

```bash
python Communication/listen_simple.py
```

### Test with Translation

```bash
python Communication/listen.py
```

## 🔧 Troubleshooting

### Common Issues

1. **"No module named 'speech_recognition'"**

   ```bash
   pip install SpeechRecognition
   ```

2. **"No module named 'pyttsx3'"**

   ```bash
   pip install pyttsx3
   ```

3. **"No module named 'pyaudio'"**

   ```bash
   pip install PyAudio
   ```

4. **Microphone not working**

   - Check microphone permissions
   - Ensure microphone is not used by other applications
   - Try running as administrator

5. **Translation not working**
   - Install googletrans: `pip install googletrans==4.0.0rc1`
   - Use `listen_simple.py` if translation is not needed

## 🎯 Integration with Main AI

```python
# In your main AI assistant
from Communication.listen_simple import SimpleVoiceListener

class JarvisAI:
    def __init__(self):
        self.listener = SimpleVoiceListener()
        self.is_running = False

    def start_listening(self):
        self.is_running = True
        self.listener.listen_continuous(self.process_command)

    def process_command(self, text, language):
        # Your AI logic here
        if "weather" in text.lower():
            self.get_weather()
        elif "time" in text.lower():
            self.get_time()
        elif "stop" in text.lower():
            self.stop()

    def stop(self):
        self.is_running = False
        self.listener.stop_listening()

# Usage
jarvis = JarvisAI()
jarvis.start_listening()
```

## 🌟 Features for Your AI Assistant

- **🎤 Continuous Listening**: Like Jarvis, listens until you stop
- **🌍 Multi-language**: Handles English and Hindi seamlessly
- **🔊 Voice Response**: Speaks back to you
- **🧠 Language Detection**: Automatically detects input language
- **⚡ Real-time**: Processes speech instantly
- **🛡️ Error Handling**: Graceful handling of errors and timeouts

Perfect for building your Iron Man-style AI assistant! 🚀
