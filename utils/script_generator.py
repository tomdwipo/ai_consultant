import json
from groq import Groq

def load_api_keys() -> dict:
    """Load API keys from config.json"""
    try:
        with open("my_config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("my_config.json not found. Please create it with your API keys.")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in my_config.json.")

def generate_script(topic: str, style: str, target_audience: str, cta: str) -> dict:
    """
    Generates a video script using Groq Cloud API with Llama3-70b-8192.
    Returns a dictionary with script and scene descriptions.
    """
    try:
        api_keys = load_api_keys()
        groq_api_key = api_keys["groq_api_key"]

        client = Groq(api_key=groq_api_key)

        prompt = f"""
        You are a creative assistant specialized in writing engaging and dynamic video scripts for TikTok. Your goal is to create scripts that maximize viewer retention. The video must:
        1. Capture attention in the first 3 seconds with a bold statement, intriguing question, or surprising fact.
        2. Deliver concise, valuable, or entertaining content in the body (50–65 seconds) using clear and energetic language with snappy pacing.
        3. Include a compelling call-to-action (CTA) in the last 10 seconds that encourages likes, shares, follows, or comments.

        Create a video script with 250 to 280 tokens based on the following details:
        - Topic: {topic}
        - Style: {style}
        - Target Audience: {target_audience}
        - CTA: {cta}

        Return the script in JSON format with the following structure:
        {{
          "script": "Full script text to be narrated by TTS",
          "scenes": [
            {{
              "scene_number": 1,
              "visual_description": "Detailed description of the visual for this scene",
              "voiceover_text": "Text to be narrated during this scene",
              "duration_seconds": 3
            }},
            ...
          ],
          "total_duration": 60
        }}

        Ensure:
        1. The script is entertaining, relatable, and uses language and pacing suitable for TikTok's short-form, attention-driven format.
        2. The script has at least 250 tokens and a maximum of 280 tokens.
        3. Scene descriptions can use up to 500 tokens.
        4. Each scene has a clear visual description and corresponding voiceover text.
        5. The total duration is exactly 60 seconds.
        """

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=1024,
            response_format={"type": "json_object"}
        )

        response = json.loads(completion.choices[0].message.content)
        
        if not all(key in response for key in ["script", "scenes", "total_duration"]):
            raise ValueError("Invalid JSON structure from API response")
            
        return response

    except json.JSONDecodeError:
        raise ValueError("Failed to parse API response as JSON")
    except Exception as e:
        raise RuntimeError(f"Script generation failed: {str(e)}")

def save_script(script_data: dict, output_path: str) -> None:
    """Save the script as a JSON file"""
    with open(output_path, "w") as f:
        json.dump(script_data, f, indent=2)
    print(f"✅ Script saved to: {output_path}")

def main():
    try:
        topic = input("Enter video topic: ")
        style = input("Enter video style (e.g., funny, educational, inspirational): ")
        target_audience = input("Enter target audience: ")
        cta = input("Enter call to action (CTA): ")
        output_path = "script.json"

        print("\n🚀 Generating script with Llama3...")
        script_data = generate_script(topic, style, target_audience, cta)
        
        save_script(script_data, output_path)

        print(f"📝 Total duration: {script_data['total_duration']} seconds")
        print(f"🎬 Number of scenes: {len(script_data['scenes'])}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()