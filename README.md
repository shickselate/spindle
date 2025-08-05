# 🧵 Spindle

**Spindle** is a story generation and immersive narrative engine for *Fusion Shift* and beyond.  
It fuses raw event data, AI-generated news stories, and visual storytelling into a seamless pipeline  
that outputs interactive media for VR display and future companion experiences.

---

## 🧭 What It Does

- Converts raw game/world events into rich, in-universe news stories using LLMs
- Generates visual prompts from those stories
- Produces immersive 180° or SBS images via ComfyUI
- Displays them in VR using WebXR with hand tracking and floating UI
- Maintains narrative continuity through memory, characters, and timeline

---

![Spindle VR Experience](https://github.com/shickselate/spindle/raw/main/media/screenshot-20250805-000412.jpg)

*A captured moment inside Spindle: the user’s own hand floats a news story above a distant moonbase,  while twin eclipsing moons cast light across the horizon.*


---

## 🔁 Workflow Overview

1. Run `main.py` calls `narrativeBuild.py`, `characterBuilder.py` and `eventGenerator.pt` to craft several raw story text file to `storygen/rawstory/`
2. Run 
   - `gen_news_from_rawstory.py`  calls Ollama and creates a 100 word story from the rawstory→ populates `newstory/`
   - `gen_prompts_from_news.py` calls Ollama and generates a image generation prompt from newstory → populates `image_prompts/`
   - `generate_images.py` → creates images in `images/`
3. feed image prompts into ComfyUI workflow `BaseWorkflow_cleaned.py` to generate images, and then expand these to wide screen (2048 x 1024) using `flux_fill_outpaint.json`
4. Open `viewer/index.html` in a WebXR-compatible browser or headset
5. Pinch fingers to explore scenes, turn right hand up to read newstories in VR 

---

![Skirmish in Gamma Verge](https://github.com/shickselate/spindle/raw/main/media/screenshot-20250805-000316.jpg)

*Spindle’s war correspondence system in action — this in-universe news report was generated  
after a space battle broke out in the Gamma Verge, driven by real gameplay events.*


---


## 🔮 Future Features

- Character memory and recurrence tracking
- Timeline search and visualisation
- Depth-based stereoscopic image rendering
- Live event ingestion from game server
- Companion-mode playback and story arcs


---

## ✨ Why "Spindle"?

Because stories are threads.  
And Spindle weaves them into something magnificent.

---



---
