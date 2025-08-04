from eventGenerator import generate_event
from narrativeBuilder import format_narrative
from datetime import datetime
from collections import deque
import os
import time
import random

RAW_OUTPUT_DIR = "../rawstory"

def save_story_to_file(story_text, character_name):
    os.makedirs(RAW_OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = f"{timestamp}_{character_name.replace(' ', '_')}"
    filename = f"{base_name}.txt"
    filepath = os.path.join(RAW_OUTPUT_DIR, filename)

    i = 1
    while os.path.exists(filepath):
        filename = f"{base_name}_{i}.txt"
        filepath = os.path.join(RAW_OUTPUT_DIR, filename)
        i += 1

    with open(filepath, "w") as f:
        f.write(story_text)
    print(f"✅ Saved to {filepath}")
    return filepath

class StoryQueue:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event):
        event["timestamp"] = datetime.utcnow().isoformat()
        self.queue.append(event)

    def process_next(self, tone="neutral"):
        if self.queue:
            event = self.queue.popleft()
            story = format_narrative(event, tone=tone)
            character = event["main_actor"]

            description = (
                f"{character['name']} is a {character['title']} of {character['faction']}. "
                f"They are known for being {', '.join(character['traits'])}."
            )

            return {
                "event": event,
                "story": story,
                "character_description": description
            }

        return None  # fallback in case the queue is empty



    def process_all(self, tone="neutral"):
        return [self.process_next(tone) for _ in range(len(self.queue))]



if __name__ == "__main__":
    q = StoryQueue()

    print("⏳ Generating sample events...")
    for _ in range(3):
        q.add_event(generate_event())
        time.sleep(random.uniform(0.3, 1.0))

    print("\n📜 Narratives from the queue:")
    results = q.process_all(tone="cinematic")  # ← store results here

    for idx, result in enumerate(results):
        if result is None:
            continue

        print("\n---")
        print(result["story"])
        print("\n🧬 Character:")
        print(result["character_description"])

        character_name = result["event"]["main_actor"]["name"]
        save_story_to_file(
            result["story"] + "\n\n" + result["character_description"],
            character_name
        )
