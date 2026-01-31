import os
from pathlib import Path
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)


def text_to_speech(text: str, output_filename: str = "output.mp3", voice: str = "Rachel") -> str:
    audio = client.text_to_speech.convert(
        text=text,
        voice_id=get_voice_id(voice),
        model_id="eleven_multilingual_v2" 
    )
    
    save(audio, output_filename)
    
    return output_filename


def get_voice_id(voice_name: str) -> str:
    
    voices = {
        "rachel": "21m00Tcm4TlvDq8ikWAM",
        "adam": "pNInz6obpgDQGcFmaJgB",
        "bella": "EXAVITQu4vr4xnSDxMaL",
        "antoni": "ErXwobaYiN019PkySvjV",
    }
    
    voice_id = voices.get(voice_name.lower())
    
    if not voice_id:
        print(f"Voice '{voice_name}' not found. Using Rachel as default.")
        return voices["rachel"]
    
    return voice_id


def main():
    sample_article = """
    Welcome to this audio article about artificial intelligence and voice technology.
    
    In recent years, AI has transformed how we interact with technology. 
    Voice assistants like Alexa and Siri have become part of our daily lives.
    But the next frontier is making AI voices indistinguishable from human speech.
    
    Companies like ElevenLabs are leading this revolution. Their technology can 
    clone voices, translate content into multiple languages, and create entirely 
    new synthetic voices that sound remarkably human.
    
    The applications are endless: audiobooks, podcasts, accessibility tools for 
    the visually impaired, and customer service agents that actually sound helpful.
    
    Thank you for listening to this demonstration of AI-powered voice synthesis.
    """
    
    text_to_speech(
        text=sample_article,
        output_filename="my_first_podcast.mp3",
        voice="Rachel"
    )
    

if __name__ == "__main__":
    main()