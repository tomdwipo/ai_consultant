# utils/caption_overlay.py
import os
from pathlib import Path
from typing import List, Dict
import json
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

def load_captions(captions_path: Path) -> List[Dict]:
    """Load captions from a JSON file."""
    try:
        with open(captions_path, "r") as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load captions: {str(e)}")

def add_captions_to_video(video_path: Path, captions_path: Path, output_path: Path) -> None:
    """
    Add captions to the video at the specified timestamps.
    """
    try:
        # Load video
        video = VideoFileClip(str(video_path))

        # Load captions
        captions = load_captions(captions_path)

        # Create text clips for each caption
        text_clips = []
        for caption in captions:
            text_clip = TextClip(
                caption["text"],
                fontsize=40,
                color="white",
                font="assets\\fonts\\EastmanRomanTrial-Black.otf",
                bg_color="black",
                size=(video.size[0], None)  # Match video width
            ).set_position(("center", "bottom")) \
             .set_start(caption["start"]) \
             .set_end(caption["end"])
            text_clips.append(text_clip)

        # Combine video and text clips
        final_video = CompositeVideoClip([video] + text_clips)

        # Export video
        final_video.write_videofile(
            str(output_path),
            fps=24,
            codec="libx264",
            audio_codec="aac",
            threads=4
        )

        print(f"✅ Video with captions saved to: {output_path}")

    except Exception as e:
        raise RuntimeError(f"Failed to add captions to video: {str(e)}")

def main(video_path: Path, captions_path: Path, output_path: Path) -> None:
    """
    Add captions to the video and save the final output.
    """
    try:
        # Validate paths
        if not video_path.exists():
            raise FileNotFoundError(f"Video file {video_path} not found")
        if not captions_path.exists():
            raise FileNotFoundError(f"Captions file {captions_path} not found")

        # Add captions to video
        print("\n📝 Adding captions to video...")
        add_captions_to_video(video_path, captions_path, output_path)

    except Exception as e:
        print(f"❌ Error: {str(e)}")