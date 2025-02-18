# utils/caption_generator.py
import os
import json
from pathlib import Path
from typing import List, Dict
import whisper
import subprocess

def check_ffmpeg_installed() -> bool:
    """Check if FFmpeg is installed and accessible."""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return True
    except Exception:
        return False


def transcribe_audio_with_whisper(audio_path: Path) -> List[Dict]:
    """
    Transcribe audio using the local Whisper base.en model with native timestamping.
    Returns a list of captions with start and end times for each word.
    """
    try:
        if not check_ffmpeg_installed():
            raise RuntimeError(
                "FFmpeg is not installed. Please install FFmpeg and add it to your system PATH. "
                "Download from https://ffmpeg.org/download.html"
            )

        print("🔍 Loading Whisper model...")
        model = whisper.load_model("small.en")

        print("🔍 Transcribing audio with word-level timestamps...")
        result = model.transcribe(
            str(audio_path),
            word_timestamps=True,  
            language="en",         
            temperature=0          
        )

        captions = []
        for segment in result["segments"]:
            for word in segment["words"]:
                captions.append({
                    "start": word["start"],
                    "end": word["end"],
                    "text": word["word"].strip()
                })

        return captions

    except Exception as e:
        raise RuntimeError(f"Failed to transcribe audio: {str(e)}")

def save_captions(captions: List[Dict], output_path: Path) -> None:
    """Save captions as a JSON file"""
    with open(output_path, "w") as f:
        json.dump(captions, f, indent=2)
    print(f"✅ Captions saved to: {output_path}")

def main(audio_path: Path, output_dir: Path) -> None:
    """
    Generate captions from audio and save them to the output directory.
    """
    try:
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file {audio_path} not found")
        
        output_dir.mkdir(parents=True, exist_ok=True)

        print("\n🔍 Generating captions with Whisper...")
        captions = transcribe_audio_with_whisper(audio_path)

        captions_path = output_dir / "captions.json"
        save_captions(captions, captions_path)

    except Exception as e:
        print(f"❌ Error: {str(e)}")