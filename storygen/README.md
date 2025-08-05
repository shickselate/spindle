# StoryGen

This folder contains the core components of Spindle’s story generation pipeline.

### How it works
- **Raw game events** (e.g. battles, discoveries, crises) are converted into structured text files in `rawstory/`.
- These are processed by local LLMs (e.g. LLaMA 3) to generate:
  - **Narrative news reports** (`newstory/`)
  - **Image prompts** for scene rendering (`image_prompts/`)

Scripts in this directory manage character creation, world logic, and the overall flow of event-to-story generation.

Eventually, this pipeline will connect directly to live game state and story continuity.
