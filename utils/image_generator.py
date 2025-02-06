import os
import requests
import json
import base64
from pathlib import Path
from typing import List, Dict

def load_api_keys(config_file: str = "my_config.json") -> Dict:
    """Load API keys from config.json"""
    try:
        with open(config_file) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file {config_file} not found")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in {config_file}")

def generate_images(image_prompts_path: str, output_dir: str) -> None:
    """
    Generate images from JSON prompts file using FLUX.1-schnell model
    Args:
        image_prompts_path: Path to JSON file with prompts
        output_dir: Directory to save generated images
    """
    # Validate paths
    image_prompts_path = Path(image_prompts_path)
    output_dir = Path(output_dir)
    
    if not image_prompts_path.exists():
        raise FileNotFoundError(f"Prompt file {image_prompts_path} not found")
    
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load API key
    config = load_api_keys()
    api_key = config["together_api_key"]

    # Load prompts
    with open(image_prompts_path, "r") as f:
        prompts_data = json.load(f)
    
    if "prompts" not in prompts_data or not isinstance(prompts_data["prompts"], list):
        raise ValueError("Invalid prompts format - expected {'prompts': [...]}")

    # Generate images
    for i, prompt_data in enumerate(prompts_data["prompts"], 1):
        print(f"🖼️  Generating image {i}/{len(prompts_data['prompts'])}...")
        
        # Build the prompt string from structured data
        prompt_text = (
            f"{prompt_data['subject']}, {', '.join(prompt_data['artform'])}, "
            f"shot with {prompt_data['device'][0]}, "
            f"style: {', '.join(prompt_data['photography_style'])}, "
            f"lighting: {', '.join(prompt_data['scene_details']['lighting'])}, "
            f"composition: {', '.join(prompt_data['scene_details']['composition'])}, "
            f"additional details: {prompt_data['additional_details']}"
        )

        # API request
        response = requests.post(
            url="https://api.together.xyz/v1/images/generations",
            headers={
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": f"Bearer {api_key}"
            },
            json={
                "model": "black-forest-labs/FLUX.1-schnell",
                "prompt": prompt_text,
                "steps": 3,
                "n": 1,
                "height": 1792,
                "width": 1008,
            },
            timeout=30
        )

        # Handle response
        if response.status_code == 200:
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                image_url = data["data"][0]["url"]
                image_response = requests.get(image_url)
                
                if image_response.status_code == 200:
                    # Generate sequential filename
                    existing_files = list(output_dir.glob("*.jpeg"))
                    next_number = len(existing_files) + 1
                    image_path = output_dir / f"{next_number}.jpeg"
                    
                    with open(image_path, "wb") as f:
                        f.write(image_response.content)
                    print(f"✅ Image saved to {image_path}")
                else:
                    print(f"⚠️ Failed to download image {i}")
            else:
                print(f"⚠️ No image data in response for prompt {i}")
        else:
            print(f"⚠️ Failed to generate image {i}")
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text}")

if __name__ == "__main__":
    # Example usage
    generate_images(
        image_prompts_path="C:\\Users\\Gabriel\\Documents\\TikTokAIVideoGenerator\\video8\\image_prompts.json",
        output_dir="generated_images"
    )