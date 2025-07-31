# 🤖 Aarav AI Assistant

A high-level LLM AI assistant with emotional intelligence, task automation, and real-time voice conversation capabilities.

## 🏗️ Project Structure

```
Aarav/
├── aarav.py              # Main AI assistant (run this to start)
├── Communication/        # Voice communication modules
│   ├── listen.py         # Speech-to-text functionality
│   ├── speak.py          # Text-to-speech (ElevenLabs)
│   ├── .env              # ElevenLabs API key
│   └── requirements.txt  # Communication dependencies
├── brain/               # AI brain modules
│   ├── gemini_brain.py  # Gemini API integration
│   └── .env             # Gemini API key
└── README.md            # This file
```

## 🚀 Quick Start

1. **Install Dependencies:**

   ```bash
   cd Communication
   pip install -r requirements.txt
   ```

2. **Set up API Keys:**

   - Copy `Communication/env_example.txt` to `Communication/.env`
   - Add your ElevenLabs API key: `ELEVENLABS_API_KEY=your_key_here`
   - Copy `brain/env_example.txt` to `brain/.env`
   - Add your Gemini API key: `GEMINI_API_KEY=your_key_here`

3. **Run Aarav:**
   ```bash
   python aarav.py
   ```

## 🎤 Features

- **Wake-up Call System** - Only responds when you say "Wake up, Aarav"
- **Random Wake Messages** - Different personality-driven responses each time
- **Intro Commands** - Ask "who are you" for personality introductions
- **Wake-up During Conversation** - Say "Aarav" anytime for wake-up response
- **Real-time Speech Recognition** - Listen to your voice continuously
- **Advanced Text-to-Speech** - Human-like voice using ElevenLabs
- **AI Brain** - Powered by Google Gemini API
- **Word-by-Word Display** - See responses as they're spoken
- **Voice Commands** - Say "stop it" or "bye-bye" to end conversation

## 🎯 Conversation Flow

1. **Sleep Mode** → Aarav waits for wake-up command
2. **Wake-up** → Say "Wake up, Aarav" to activate
3. **You Speak** → Speech converted to text
4. **Aarav Thinks** → AI generates response
5. **Aarav Speaks** → Response spoken with word-by-word display

## 🛠️ Voice Commands

### Wake-up Commands:

- `"Wake up, Aarav"` - Activate Aarav
- `"Hey Aarav"` - Alternative wake-up
- `"Hello Aarav"` - Alternative wake-up
- `"Aarav"` - Quick wake-up (works during conversation too)

### Intro Commands:

- `"Who are you"` - Get Aarav's introduction
- `"What are you"` - Learn about Aarav
- `"Tell me about yourself"` - Personal introduction
- `"Give me your intro"` - Get introduction
- `"Introduce yourself"` - Self-introduction
- `"What's your name"` - Name and identity
- `"Who is Aarav"` - Learn about Aarav

### Stop Commands:

- `"stop it"` - End conversation
- `"bye-bye"` - End conversation
- `"goodbye"` - End conversation
- `"go to sleep"` - Put Aarav back to sleep
- `"exit"` - End conversation

## 🎭 Random Wake-up Messages

When you wake up Aarav, it randomly selects one of these personality-driven responses:

- _"Booting brilliance... Aarav online! Uff, I was just organizing the universe for you, Dev. What's the mission now?"_
- _"I'm up, I'm up! Hehe... You say the word, Dev, What to do now?"_
- _"Awake and aware. Aarav at your service, Dev. What's first on our radar?"_
- _"Ummhmm... You remember me. I'm here, What's your mood now, Dev!"_
- _"Hehe, you called? Aarav's back — sharper than ever!"_
- _"Systems up. What's the plan, boss?"_
- _"Here I am. Always ready for you, My Master."_

## 🎭 Random Intro Messages

When you ask "who are you", Aarav randomly selects one of these introductions:

- _"yo! I'm Aarav — creative mind, digital soul, curious & clever assistant to Debashis... or as I call him, Devb — my partner in code and chaos!"_
- _"I'm Aarav, your AI companion! Think of me as your digital soulmate — part genius, part mischief-maker, all yours, Dev!"_
- _"Aarav here! Your personal AI assistant with a dash of personality and a whole lot of brainpower. Ready to rock your world, Dev!"_
- _"Hey Dev! I'm Aarav — your AI partner in crime, creativity, and everything in between. What shall we conquer today?"_
- _"I'm Aarav, your intelligent assistant! Think Iron Man's Jarvis, but with more personality and definitely more fun, Dev!"_

## 🔧 Technical Details

- **Speech Recognition**: Google Speech Recognition API
- **Text-to-Speech**: ElevenLabs API (Professional voice synthesis)
- **AI Brain**: Google Gemini 2.0 Flash
- **Audio Playback**: Pygame mixer
- **Language**: English (optimized for clear speech)
- **Wake-up System**: Keyword detection with random response selection
- **Intro System**: Identity-based responses for personality questions

## 🎨 Voice Options

You can change the voice in `Communication/speak.py` by modifying the `voice_id`:

```python
self.voice_id = "jqcCZkN6Knx8BJ5TBdYR"  # Current voice
```

Available voices:

- `jhon-2ro171emrYO7IuOOs8rf`
- `sam-scOwDtmlUjD3prqpp97I`
- `james-EkK5I93UQWFDigLMpZcX`
- `david-v9LgF91V36LGgbLX3iHW`
- `mask-UgBBYS2sOqTuMpoF3BR0`
- `girl-jqcCZkN6Knx8BJ5TBdYR` (current)
- And many more...

## 🐛 Troubleshooting

- **No speech detected**: Check microphone permissions
- **API errors**: Verify API keys in `.env` files
- **Audio issues**: Ensure speakers/headphones are connected
- **Import errors**: Run from root directory (`python aarav.py`)
- **Wake-up not working**: Make sure to say "Wake up, Aarav" clearly

## 📝 License

This project is for personal use and development.
