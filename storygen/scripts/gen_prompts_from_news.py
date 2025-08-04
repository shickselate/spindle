import os
import ollama

INPUT_DIR = "../newstory"
OUTPUT_DIR = "../image_prompts"
MODEL_NAME = "llama3"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_image_prompt(news_text):
    prompt = f"""Based on this short in-universe news story, write a visually descriptive prompt suitable for AI image generation. Focus on one clear scene. Use present tense. Example: "A battle-damaged space cruiser floats in orbit, with sparks and smoke trailing." Keep it concise.

Story:
{news_text}

Prompt:"""
    response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return response['message']['content'].strip()

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(INPUT_DIR, filename), 'r', encoding='utf-8') as file:
            news_text = file.read()
        image_prompt = generate_image_prompt(news_text)
        out_path = os.path.join(OUTPUT_DIR, filename)
        with open(out_path, 'w', encoding='utf-8') as file:
            file.write(image_prompt)
        print(f"✅ Created image prompt for {filename}")
