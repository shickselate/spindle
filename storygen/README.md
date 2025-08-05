# StoryGen

![Jalen Zirra – Storybirth](https://github.com/shickselate/spindle/blob/main/viewer/assets/images/20250803_204414_Jalen_Zirra.png)

*Every story begins with a signal —  
an event, a name, a ripple in the world.*

---

This folder contains the core components of Spindle’s story generation system.

### How it works
- **Raw game events** (e.g. battles, landings, discoveries) are stored in `rawstory/`.
- Local LLMs process them into:
  - Narrative news reports (`newstory/`)
  - Image prompts for scene generation (`image_prompts/`)

Scripts here manage character creation, event logic, and narrative formatting.

Eventually, this pipeline will connect to live game data and long-term continuity.
