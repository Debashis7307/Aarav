# TTS Provider Switching Guide

## Current Setup: Murf Text-to-Speech ✅

### Voice Configuration:
- **Provider**: Murf AI
- **Voice ID**: `en-US-natalie`
- **Style**: `Inspirational`
- **API Key**: `MURF_API_KEY` (in .env file)
- **Previous Voice**: `en-US-ken` (Conversational) - commented out for easy switching

---

## How to Switch to ElevenLabs

### Step 1: Update speak.py
In `Communication/speak.py`, make these changes:

1. **Comment out MurfSpeaker class** (lines ~39-97):
   ```python
   # class MurfSpeaker:
   #     def __init__(self):
   #         ...
   ```

2. **Uncomment ElevenLabsSpeaker class** (lines ~99-179):
   ```python
   class ElevenLabsSpeaker:
       def __init__(self):
           ...
   ```

3. **Update get_speaker() function** (around line 190):
   ```python
   def get_speaker():
       global _speaker
       if _speaker is None:
           # _speaker = MurfSpeaker()  # COMMENT THIS
           _speaker = ElevenLabsSpeaker()  # UNCOMMENT THIS
       return _speaker
   ```

### Step 2: Update .env file
In `Communication/.env`, change:
```
# From:
MURF_API_KEY=ap2_a4093b81-b8eb-478b-9263-776a37a9eb0c

# To:
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

### Step 3: Install dependencies (if needed)
```bash
# ElevenLabs uses requests (already installed)
# No additional packages needed
```

---

## How to Switch Back to Murf

### Step 1: Update speak.py
1. **Uncomment MurfSpeaker class** (lines ~39-97)
2. **Comment out ElevenLabsSpeaker class** (lines ~99-179)
3. **Update get_speaker() function**:
   ```python
   _speaker = MurfSpeaker()  # UNCOMMENT THIS
   # _speaker = ElevenLabsSpeaker()  # COMMENT THIS
   ```

### Step 2: Update .env file
```
MURF_API_KEY=ap2_a4093b81-b8eb-478b-9263-776a37a9eb0c
```

### Step 3: Install Murf SDK
```bash
pip install murf
```

---

## Voice Options

### Murf Voices:
- `en-US-ken` (Current - Male, Conversational)
- `en-US-natalie` (Female)
- `en-US-terrell` (Male)
- And many more...

### ElevenLabs Voices:
- `jqcCZkN6Knx8BJ5TBdYR` (Rachel - clear, friendly)
- `scOwDtmlUjD3prqpp97I` (Sam)
- `EkK5I93UQWFDigLMpZcX` (James)
- And many more...

---

## Quick Test Commands

```bash
# Test current setup
python Communication/test_setup.py

# Test voice functionality
python Communication/test_murf.py

# Run Aarav
python aarav.py
```