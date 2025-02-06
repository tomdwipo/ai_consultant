# utils/video_composer.py
import os
from pathlib import Path
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip
from moviepy.video.fx.all import fadein, fadeout
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

def calculate_image_duration(audio_path: Path, num_images: int) -> float:
    """
    Calculate the duration each image should be displayed based on audio length.
    """
    try:
        audio = AudioFileClip(str(audio_path))
        audio_duration = audio.duration
        return audio_duration / num_images
    except Exception as e:
        raise RuntimeError(f"Failed to calculate image duration: {str(e)}")

def create_video_clip(image_folder: Path, audio_path: Path, output_path: Path) -> None:
    """
    Create a video from images and audio.
    """
    try:
        # Load images
        image_files = sorted(image_folder.glob("*.jpeg"))
        if not image_files:
            raise ValueError("No images found in the specified folder")

        # Calculate image duration
        image_duration = calculate_image_duration(audio_path, len(image_files))
        print(f"⏱️  Each image will be displayed for {image_duration:.2f} seconds")

        # Create image clips with transitions
        clips = []
        for i, image_file in enumerate(image_files):
            clip = ImageSequenceClip([str(image_file)], durations=[image_duration])
            
            # Add fade transitions (except for the first and last clips)
            if i > 0:
                clip = fadein(clip, 0.5)  # Fade in over 0.5 seconds
            if i < len(image_files) - 1:
                clip = fadeout(clip, 0.5)  # Fade out over 0.5 seconds
            
            clips.append(clip)

        # Combine clips
        video = concatenate_videoclips(clips, method="compose")

        # Add audio
        audio = AudioFileClip(str(audio_path))
        video = video.set_audio(audio)

        # Export video
        video.write_videofile(
            str(output_path),
            fps=24,  # Standard frame rate
            codec="libx264",  # H.264 codec
            audio_codec="aac",  # AAC audio codec
            threads=4  # Use multiple threads for faster rendering
        )

        print(f"✅ Video saved to: {output_path}")

    except Exception as e:
        raise RuntimeError(f"Failed to create video: {str(e)}")

def main(image_folder: Path, audio_path: Path, output_path: Path) -> None:
    """
    Generate a video from images and audio.
    """
    try:
        create_video_clip(image_folder, audio_path, output_path)
    except Exception as e:
        print(f"❌ Error: {str(e)}")