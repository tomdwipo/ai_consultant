import os
from pathlib import Path
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip
from moviepy.video.fx.all import fadein, fadeout
from moviepy.config import change_settings

# change_settings({"IMAGEMAGICK_BINARY": r"/Users/tommy-amarbank/Documents/startup/TikTokAIVideoGenerator/ImageMagick-7.0.10/bin/magick"})

# change_settings({"IMAGEMAGICK_BINARY": r"ImageMagick-7.0.10/bin/magick"})

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
        image_files = sorted(image_folder.glob("*.jpeg"))
        if not image_files:
            raise ValueError("No images found in the specified folder")

        image_duration = calculate_image_duration(audio_path, len(image_files))
        print(f"⏱️  Each image will be displayed for {image_duration:.2f} seconds")

        clips = []
        for i, image_file in enumerate(image_files):
            clip = ImageSequenceClip([str(image_file)], durations=[image_duration])
            
            if i > 0:
                clip = fadein(clip, 0.5)  
            if i < len(image_files) - 1:
                clip = fadeout(clip, 0.5) 
            
            clips.append(clip)

        video = concatenate_videoclips(clips, method="compose")

        audio = AudioFileClip(str(audio_path))
        video = video.set_audio(audio)

        video.write_videofile(
            str(output_path),
            fps=30,  
            codec="libx264",  
            audio_codec="aac", 
            threads=4  
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