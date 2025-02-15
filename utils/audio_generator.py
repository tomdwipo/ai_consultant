import json
import os
import requests
from pathlib import Path
from typing import Optional
import edge_tts
import asyncio

def generate_audio_kokoro(text: str, output_path: Path, voice: str = "af_bella") -> bool:
    """
    Generate audio using Kokoro TTS API.
    Returns True if successful, False otherwise.
    """
    try:
        response = requests.post(
            "https://api.kokorotts.com/v1/audio/speech",
            json={
                "model": "kokoro", 
                "input": text,
                "voice": voice,
                "response_format": "mp3",
                "speed": 1.0
            },
            timeout=30  
        )

        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Audio generated using Kokoro TTS: {output_path}")
            return True
        else:
            print(f"⚠️ Kokoro TTS API error: {response.status_code} - {response.text}")
            return False

    except Exception as e:
        print(f"⚠️ Kokoro TTS API failed: {str(e)}")
        return False

async def generate_audio_edge(text: str, output_path: Path) -> bool:
    """
    Generate audio using Edge TTS as a fallback.
    Returns True if successful, False otherwise.
    """
    try:
        communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
        await communicate.save(output_path)
        print(f"✅ Audio generated using Edge TTS: {output_path}")
        return True

    except Exception as e:
        print(f"⚠️ Edge TTS failed: {str(e)}")
        return False

def generate_audio(text: str, output_path: Path, voice: str = "af_bella") -> bool:
    """
    Generate audio using Kokoro TTS (with fallback to Edge TTS).
    Returns True if successful, False otherwise.
    """
    for attempt in range(2):
        if generate_audio_kokoro(text, output_path, voice):
            return True
        print(f"Retrying Kokoro TTS... (Attempt {attempt + 1}/2)")

    print("⚠️ Kokoro TTS unavailable. Falling back to Edge TTS...")
    return asyncio.run(generate_audio_edge(text, output_path))

def main(script_path: Path, output_dir: Path) -> None:
    """
    Generate audio from script and save it to the output directory.
    """
    try:
        with open(script_path, "r") as f:
            script_data = json.load(f)
        
        script_text = script_data.get("script", "")
        if not script_text:
            raise ValueError("Script text is empty")

        output_dir.mkdir(parents=True, exist_ok=True)

        audio_path = output_dir / "voiceover.mp3"
        if not generate_audio(script_text, audio_path):
            raise RuntimeError("Failed to generate audio using both Kokoro and Edge TTS")

        print(f"✅ Audio saved to: {audio_path}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")