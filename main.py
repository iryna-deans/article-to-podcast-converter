"""Convert text to speech using ElevenLabs API."""

import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

load_dotenv()


def text_to_speech(text: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM") -> None:
    """Convert text to speech and save as MP3."""
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise ValueError("Set ELEVENLABS_API_KEY in your .env file")
    
    client = ElevenLabs(api_key=api_key)
    
    audio = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",
    )
    
    save(audio, "output.mp3")


if __name__ == "__main__":
    sample = "Hello! This is a test of the ElevenLabs text to speech API."
    text_to_speech(sample)