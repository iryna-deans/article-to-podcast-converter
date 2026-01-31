# Article to Podcast Converter

A simple Python tool that converts text articles into natural-sounding audio podcasts using the ElevenLabs API.

## Features

- Convert any text to natural-sounding speech
- Multiple voice options (Rachel, Adam, Bella, Antoni)
- High-quality audio output using ElevenLabs' multilingual v2 model
- Simple, clean Python code with type hints

## Tech Stack

- Python 3.11+
- ElevenLabs API
- python-dotenv for environment management

## Getting Started

### Prerequisites

- Python 3.11 or higher
- An ElevenLabs account (free tier works)

### Installation

1. Clone this repository:
```bash
   git clone https://github.com/YOUR_USERNAME/elevenlabs-article-to-podcast.git
   cd elevenlabs-article-to-podcast
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate 
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file with your ElevenLabs API key:
```
   ELEVENLABS_API_KEY=your_api_key_here
```

5. Run the converter:
```bash
   python main.py
```

