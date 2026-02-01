"""
Voice comparison tool - Generate the same text with different ElevenLabs voices.

Useful for finding the right voice for your project by hearing them side-by-side.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

load_dotenv()


VOICES = {
    "rachel": "21m00Tcm4TlvDq8ikWAM",    
    "adam": "pNInz6obpgDQGcFmaJgB",      
    "bella": "EXAVITQu4vr4xnSDxMaL",     
}


def compare_voices(text: str, output_dir: str = "comparisons") -> list[str]:
    """
    Generate audio samples of the same text using different voices.
    
    Returns list of created file paths.
    """
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise ValueError("Set ELEVENLABS_API_KEY in your .env file")
    
    client = ElevenLabs(api_key=api_key)
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    created_files = []
    
    for voice_name, voice_id in VOICES.items():
        print(f"Generating with {voice_name}...")
        
        audio = client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
        )
        
        filename = output_path / f"{voice_name}_sample.mp3"
        save(audio, str(filename))
        created_files.append(str(filename))
        
        print(f"  ✓ Saved: {filename}")
    
    return created_files


def main():
    sample_text = """
    Welcome to the future of voice technology. Today we're exploring how 
    artificial intelligence is transforming the way we create and consume 
    audio content. From podcasts to audiobooks, the possibilities are endless.
    """
        
    files = compare_voices(sample_text.strip())
    
if __name__ == "__main__":
    main()