# TikTok AI Video Generator

This project is a Python-based tool for generating vertical videos optimized for platforms like TikTok, Instagram Reels, and YouTube Shorts. It uses AI models for script generation, image creation, audio synthesis, and captioning to automate the video creation process.

---

## Features

- **Script Generation**: Create engaging video scripts using Llama3 via the Groq Cloud API.
- **Image Generation**: Generate high-quality images using Together AI's FLUX-1 model.
- **Audio Generation**: Convert scripts to audio using Kokoro TTS (with fallback to Edge TTS).
- **Caption Generation**: Transcribe audio to captions using OpenAI's Whisper model.
- **Video Composition**: Combine images, audio, and captions into a final video using MoviePy.
- **User Choice**: Choose between generating a full video or just the script, images, and audio.

---

## Prerequisites

Before running the project, ensure you have the following:

1. **Python 3.11**: Install Python from [python.org](https://www.python.org/downloads/release/python-3110/).
2. **API Keys**:
   - Groq Cloud API key (for script generation).
     [GroqCloud](https://console.groq.com/login)
   - Together AI API key (for image generation).
     [Together AI](https://www.together.ai/)
3. **FFmpeg**: Required for audio and video processing. Download from [ffmpeg.org](https://ffmpeg.org/).
4. **ImageMagick**: Required for video processing. Download from [ImageMagick](https://imagemagick.org/script/download.php).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tiktok-ai-video-generator.git
   cd tiktok-ai-video-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up API keys:
   - Rename your  `config.json` file in the project root for `my_config.json`, make sure the archive is with the following structure:
     ```json
     {
       "groq_api_key": "your-groq-api-key",
       "together_api_key": "your-together-api-key"
     }
     ```

4. Install FFmpeg:
   - Download and install FFmpeg from [ffmpeg.org](https://ffmpeg.org/).
   - Add FFmpeg to your system PATH.

5. Install ImageMagick:
   - Download and install ImageMagick from [ImageMagick](https://imagemagick.org/script/download.php).
   - Make sure ImageMagick's folder is on this path.
     ```bash
     C:\Program Files\ImageMagick-7.1.1-Q16-HDRI
     ```

---

## Usage

Run the program:
```bash
python main.py
```

### Workflow

1. **Input Details**:
   - Enter the project folder name, video topic, style, target audience, and call-to-action (CTA).

2. **Choose Option**:
   - Select `1` for a full video (script + images + audio + captions + final video).
   - Select `2` for a partial video (script + images + audio).

3. **Generated Files**:
   - The project folder will contain:
     - `script.json`: Generated script.
     - `image_prompts.json`: Image prompts.
     - `images/`: Generated images.
     - `audio/voiceover.mp3`: Generated audio.
     - `captions/captions.json`: Generated captions (if full video is selected).
     - `final_video.mp4`: Video without captions (if full video is selected).
     - `final_video_with_captions.mp4`: Final video with captions (if full video is selected).

---

## Workflow Details

### 1. Script Generation
- Uses Llama3 via the Groq Cloud API to generate a script based on user inputs.
- Saves the script as `script.json`.

### 2. Image Prompt Generation
- Creates image prompts based on the script.
- Saves the prompts as `image_prompts.json`.

### 3. Image Generation
- Uses Together AI's FLUX-1 model to generate images.
- Saves images in the `images/` folder.

### 4. Audio Generation
- Uses Kokoro TTS to generate audio from the script.
- Falls back to Edge TTS if Kokoro TTS fails.
- Saves the audio as `audio/voiceover.mp3`.

### 5. Caption Generation (Full Video Only)
- Uses OpenAI's Whisper model to transcribe audio into captions.
- Saves captions as `captions/captions.json`.

### 6. Video Composition (Full Video Only)
- Combines images, audio, and captions into a final video.
- Saves the video as `final_video_with_captions.mp4`.

---

## Customization

### Subtitles
- Subtitles are split into a maximum of 5 words per line and truncated into 2 lines.
- Font: Arial-Bold, size 50.
- White text with a black stroke for better contrast.
- Positioned at the bottom center of the video.

### Video Format
- Resolution: 1080x1920 (vertical format).
- Frame rate: 24 FPS.
- Codec: H.264 for video, AAC for audio.

---

## Troubleshooting

### Kokoro TTS Fails
- If Kokoro TTS fails, the program automatically falls back to Edge TTS.

### FFmpeg Not Found
- Ensure FFmpeg is installed and added to your system PATH.

### API Errors
- Verify that your API keys are correct and have sufficient credits.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Llama3**: For script generation.
- **Together AI**: For image generation.
- **Kokoro TTS**: For audio synthesis.
- **OpenAI Whisper**: For caption generation.
- **MoviePy**: For video composition.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## Contact

For questions or feedback, contact [gabriel_laxy@proton.me](mailto:gabriel_laxy@proton.me).
