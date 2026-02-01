# Article to Podcast Converter

A simple Python tool that converts text articles into natural-sounding audio podcasts using the ElevenLabs API.

## Tech Stack

- Python 3.11+
- ElevenLabs API
- python-dotenv for environment management

## Getting Started

### Prerequisites

- Python 3.11 or higher
- An ElevenLabs account 

### Installation

1. Clone this repository:

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your ElevenLabs API key (use .env.example)
```
ELEVENLABS_API_KEY=your_api_key_here
```

5. Run the converter:
```bash
python main.py
```

## Voice Comparison Tool

Not sure which voice to use? Generate samples with multiple voices:
```bash
python compare_voices.py
```

This creates MP3 files in `/comparisons` so you can listen and compare.

### Available Voices

| Voice | Style | Best For |
|-------|-------|----------|
| Rachel | Calm, clear | Narration, explainers |
| Adam | Deep, authoritative | News, documentaries |
| Bella | Soft, warm | Storytelling, gentle content |