# main.py
import os
from pathlib import Path
from utils.script_generator import generate_script, save_script
from utils.image_prompt_generator import main as generate_image_prompts
from utils.image_generator import generate_images
from utils.audio_generator import main as generate_audio
from utils.video_composer import main as create_video
from utils.caption_generator import main as generate_captions
from utils.caption_overlay import main as add_captions

def create_project_folder(folder_name: str) -> Path:
    """Create a folder for the project and return its path"""
    project_path = Path(folder_name)
    project_path.mkdir(parents=True, exist_ok=True)
    (project_path / "images").mkdir(exist_ok=True)  # Create images subfolder
    (project_path / "audio").mkdir(exist_ok=True)  # Create audio subfolder
    (project_path / "captions").mkdir(exist_ok=True)  # Create captions subfolder
    return project_path

def main():
    try:
        print("""
 █████╗ ██╗    ██╗   ██╗██╗██████╗ ███████╗ ██████╗                          
██╔══██╗██║    ██║   ██║██║██╔══██╗██╔════╝██╔═══██╗                         
███████║██║    ██║   ██║██║██║  ██║█████╗  ██║   ██║                         
██╔══██║██║    ╚██╗ ██╔╝██║██║  ██║██╔══╝  ██║   ██║                         
██║  ██║██║     ╚████╔╝ ██║██████╔╝███████╗╚██████╔╝                         
╚═╝  ╚═╝╚═╝      ╚═══╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝                          
                                                                             
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")
        # User inputs
        folder_name = input("Enter the name of the folder to save the project: ").strip()
        topic = input("Enter video topic: ")
        style = input("Enter video style (e.g., funny, educational, inspirational): ")
        target_audience = input("Enter target audience: ")
        cta = input("Enter call to action (CTA): ")
        
        # Create project folder
        project_path = create_project_folder(folder_name)
        print(f"✅ Created project folder at: {project_path}")

        # File paths
        script_path = project_path / "script.json"
        image_prompts_path = project_path / "image_prompts.json"
        images_dir = project_path / "images"
        audio_dir = project_path / "audio"
        captions_dir = project_path / "captions"
        video_path = project_path / "final_video.mp4"
        final_video_path = project_path / "final_video_with_captions.mp4"

        # Step 1: Generate script
        print("\n🚀 Generating script with Llama3...")
        script_data = generate_script(topic, style, target_audience, cta)
        save_script(script_data, script_path)

        # Step 2: Generate image prompts
        print("\n🎨 Generating image prompts...")
        generate_image_prompts(script_path, image_prompts_path)

        # Step 3: Generate images
        print("\n🌄 Generating images with FLUX-1...")
        generate_images(image_prompts_path, images_dir)

        # Step 4: Generate audio
        print("\n🔊 Generating audio...")
        generate_audio(script_path, audio_dir)

        # Step 5: Generate captions
        print("\n🔍 Generating captions...")
        generate_captions(audio_dir / "voiceover.mp3", captions_dir)

        # Step 6: Compose video
        print("\n🎥 Composing video...")
        create_video(images_dir, audio_dir / "voiceover.mp3", video_path)

        # Step 7: Add captions to video
        print("\n📝 Adding captions to video...")
        add_captions(video_path, captions_dir / "captions.json", final_video_path)

        # Print summary
        print(f"\n📝 Total duration: {script_data['total_duration']}s")
        print(f"🎬 Number of scenes: {len(script_data['scenes'])}")
        print(f"🖼️  Generated images: {len(list(images_dir.glob('*.jpeg')))}/20")
        print(f"🔊 Audio generated: {os.path.exists(audio_dir / 'voiceover.mp3')}")
        print(f"🔍 Captions generated: {os.path.exists(captions_dir / 'captions.json')}")
        print(f"🎥 Video generated: {os.path.exists(video_path)}")
        print(f"🎥 Video with captions generated: {os.path.exists(final_video_path)}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()