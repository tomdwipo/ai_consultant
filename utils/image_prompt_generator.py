# utils/image_prompt_generator.py
import json
from pathlib import Path
from groq import Groq
from typing import List, Dict

def load_api_keys() -> dict:
    """Load API keys from config.json in root folder"""
    try:
        root_dir = Path(__file__).resolve().parent.parent
        config_path = root_dir / "my_config.json"
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("my_config.json not found in root folder")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in my_config.json")

def generate_image_prompts(script_data: Dict) -> List[Dict]:
    """
    Generate 18-20 image prompts using Llama3.3 and the provided metadata schema.
    Returns a list of image prompts following the specified structure.
    """
    try:
        # Load API keys
        api_keys = load_api_keys()
        groq_api_key = api_keys["groq_api_key"]

        # Initialize Groq client
        client = Groq(api_key=groq_api_key)

        # Extract script elements
        scenes = script_data.get("scenes", [])
        script_text = script_data.get("script", "")

        # Create explicit structured prompt
        prompt = f"""
        You are a creative assistant specialized in generating image prompts for AI image generation models. 
        Create between 18-20 image prompts based on the following video script and scenes:

        VIDEO SCRIPT:
        {script_text}

        SCENES:
        {json.dumps(scenes, indent=2)}

        Use this EXACT response format:
        {{
          "prompts": [
            {{
              "subject": "cosmic singularity",
              "artform": ["digital_artform"],
              "phototype": ["wide angle"],
              "scene_details": {{
                "place": ["cosmic environment"],
                "lighting": ["neon"],
                "composition": ["dynamic angles"]
              }},
              "background": ["shallow depth of field"],
              "additional_details": {{
                "wearing": "energy field",
                "holding": "quantum particles"
              }},
              "photography_style": ["concept art"],
              "device": ["Sony Alpha 1"],
              "artist": ["Beeple"]
            }},
            // REPEAT FOR 20 PROMPTS
          ]
        }}

        Rules:
        1. Generate 20 prompts
        2. Maintain the JSON structure strictly
        3. Ensure all prompts follow the metadata schema
        4. No markdown formatting, only pure JSON
        """

        # Make API call with higher token limit
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=4096, 
            response_format={"type": "json_object"}
        )

        # Parse and validate response
        response = json.loads(completion.choices[0].message.content)
        
        # Debugging: Print raw response
        # print("Raw API response:", json.dumps(response, indent=2))
        
        # Flexible validation
        prompts = response.get("prompts") or response  # Handle root array responses
        
        # Validate prompt count
        MIN_PROMPTS = 18
        MAX_PROMPTS = 25
        if not isinstance(prompts, list) or not (MIN_PROMPTS <= len(prompts) <= MAX_PROMPTS):
            raise ValueError(
                f"Invalid response format. Got {len(prompts) if isinstance(prompts, list) else 0} prompts. "
                f"Expected between {MIN_PROMPTS}-{MAX_PROMPTS} prompts."
            )
            
        # Validate individual prompt structure
        required_keys = {"subject", "artform", "phototype", "scene_details"}
        for i, prompt in enumerate(prompts):
            if not all(key in prompt for key in required_keys):
                raise ValueError(f"Prompt {i+1} missing required keys: {required_keys}")

        return prompts

    except json.JSONDecodeError:
        raise ValueError("Failed to parse API response as JSON")
    except Exception as e:
        raise RuntimeError(f"Image prompt generation failed: {str(e)}")

def save_image_prompts(prompts: List[Dict], output_path: Path) -> None:
    """Save the image prompts as a JSON file"""
    with open(output_path, "w") as f:
        json.dump({"prompts": prompts}, f, indent=2)
    print(f"✅ Saved {len(prompts)} image prompts to: {output_path}")

def main(script_path: Path, output_path: Path) -> None:
    """Generate and save image prompts"""
    try:
        # Load script
        with open(script_path, "r") as f:
            script_data = json.load(f)
        
        # Generate prompts
        prompts = generate_image_prompts(script_data)
        
        # Save prompts
        save_image_prompts(prompts, output_path)
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")