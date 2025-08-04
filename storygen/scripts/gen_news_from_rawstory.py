import os
import ollama

INPUT_DIR = "../rawstory"
OUTPUT_DIR = "../newstory"
MODEL_NAME = "llama3"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_news_report(story):
    prompt = f"""Write a short in-universe news report based on the following sci-fi event summary. Keep it factual and concise, no longer than 100 words. Format it like a headline and article.

Event Summary:
{story}
"""
    response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(INPUT_DIR, filename), "r", encoding="utf-8") as f:
            story = f.read()

        news = generate_news_report(story)

        # No filename change — reuse base
        output_file = os.path.join(OUTPUT_DIR, filename)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(news)

        print(f"✅ Saved news report: {output_file}")
