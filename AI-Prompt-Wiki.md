# Prompt Templates

Short reference library of reusable prompts pulled from the video guides.

## Index

- [Adobe Firefly](#adobe-firefly)
	- [Base engineering concept](#base-engineering-concept)
	- [Canvas expansion](#canvas-expansion)
- [AutoSubs AI (DaVinci Resolve & Premiere Pro)](#autosubs-ai-davinci-resolve--premiere-pro)
    - [Model selection cheat sheet](#model-selection-cheat-sheet)
    - [Short-form subtitle formatting](#short-form-subtitle-formatting)
- [Edge Copilot](#edge-copilot)
	- [Read active tabs](#read-active-tabs)
	- [Synthesize for Notion](#synthesize-for-notion)
- [GitHub Copilot](#github-copilot)
	- [Refactor hardware logic](#refactor-hardware-logic)
	- [Fix compilation error](#fix-compilation-error)
- [Google NotebookLM](#google-notebooklm)
	- [Socratic tutor prompt](#socratic-tutor-prompt)
- [Upscayl](#upscayl)
    - [Ultra Sharp (General & Diagrams)](#ultra-sharp-general--diagrams)
    - [UltraMix Balanced (Mixed Graphics & CGI)](#ultramix-balanced-mixed-graphics--cgi)
    - [Digital Art / Anime (Clean Graphics)](#digital-art--anime-clean-graphics)

## Adobe Firefly

### Base engineering concept

What it does: Creates a detailed futuristic hydroponics scene that works well as a polished presentation background.

Best for: Starting a clean, professional visual from scratch before making smaller edits.

```text
A complex futuristic hydroponics system inside a transparent glass dome, stylized blueprints floating around it, high-tech sensors, clean engineering aesthetic, soft blue and green lighting, corporate visualization style, 8k resolution --ar 16:9
```

### Canvas expansion

What it does: Extends the image so the scene feels wider and leaves more empty space for titles or bullet points.

Best for: Turning a tight image into a slide-friendly widescreen layout.

```text
Seamless extension of the clean engineering lab environment, minimalist white desk surface, more subtle geometric blueprint patterns receding into the soft focus background
```

## AutoSubs AI (DaVinci Resolve & Premiere Pro)

### Model selection cheat sheet

What it does: Details the optimal local speech-to-text AI models inside AutoSubs for different hardware setups and project requirements.

Best for: Choosing the right transcription engine for speed, language support, or offline execution without paying cloud API fees.

* **Parakeet Model (Fastest / English Only):** * *Best for:* Fast English transcriptions, short-form voiceovers (e.g., Voicebox AI narrations), and low-tier laptops.
* *Perks:* Ultra-lightweight on VRAM, near-instant rendering speeds, and word-level timestamp accuracy.


* **Whisper Small / Medium (Multi-Language / Balanced):** * *Best for:* Multi-language content, Accented English, and complex terminology.
* *Perks:* High recognition accuracy even with background music or noise; runs locally on consumer GPUs.


* **Whisper Large (Maximum Accuracy):** * *Best for:* Long-form lectures, multi-speaker interviews, and noisy environments.
* *Perks:* Highest accuracy; requires higher GPU VRAM.



### Short-form subtitle formatting

What it does: Configures AutoSubs to output bite-sized subtitle blocks optimal for TikTok, YouTube Shorts, and Instagram Reels.

Best for: Generating readable, high-impact 2–4 word subtitle tracks on 9:16 vertical video timelines.

```text
Target Platform: DaVinci Resolve (Text+ Track V2) / Adobe Premiere Pro (Essential Graphics)
Target Format: 9:16 Vertical Shorts
Language: English
Model: Parakeet (or Whisper Small)
Max Characters Per Line: 15 - 20
Max Lines Per Block: 1
Animation Style: Pop-in Zoom / High-contrast Stroke & Shadow

```

> **Platform Integration Notes:**
> * **DaVinci Resolve:** Launch via `Workspace` → `Scripts` → `AutoSubs`. Outputs editable, keyframeable `Text+` title blocks natively onto Video Track 2 (`V2`) on both the **Free** and **Studio** versions of Resolve.
> * **Adobe Premiere Pro:** Integrates as a local panel script/extension. Exports SRT files or generates native Essential Graphics caption clips directly on the Premiere timeline.
> 
> 



## Edge Copilot

### Read active tabs

What it does: Asks Copilot to read the documents already open in your browser and summarize the main idea.

Best for: Quickly understanding assignment pages or rubrics without copying the text manually.

```text
I have opened my SDM Assignment Brief in Tab 1 and the Assessment Rubric in Tab 2. Please scan the content of both active tabs. Acknowledge if you can read them by replying with "Ready", and summarize the main objective of the assignment in one sentence.
```

### Synthesize for Notion

What it does: Turns several class documents into one organized progress tracker that is easy to paste into Notion.

Best for: Planning coursework, tracking milestones, and breaking a big assignment into smaller steps.

```markdown
Act as an expert Academic Project Manager. Synthesize the information from my active tabs (Assignment Brief, Rubric, and Lesson Plan) to create a structured execution tracker.

OUTPUT REQUIREMENT:
Generate a single Markdown table that functions as a **progress tracker with cumulative grading logic and checkboxes**, suitable for direct use in Notion.

TABLE COLUMNS (in exact order):
1. Status (use ONLY: 🟥 Not Started / 🟨 In Progress / 🟩 Done)
2. Phase / Milestone
3. Key Deliverable (clear, concise, action-based)
4. Incremental % (portion of total assignment marks)
5. Cumulative Progress (%) (running total that reaches exactly 30%)
6. Week

CRITICAL RULES:
- Use standard Markdown table syntax only (no HTML, no merged cells).
- Ensure cumulative % increases logically and ends at EXACTLY 30%.
- Accurately distribute weight:
	- Task 1 = 20%
	- Task 2 = 10%
- Each row must represent a **real actionable step**, not generic phases.
- Sort rows chronologically based on the lesson plan timeline.
- Include clear milestone markers:
	- “✅ Task 1 Done” at 20%
	- “✅ FINAL” at 30%

FORMATTING RULES (VERY IMPORTANT):
- Status must be a separate column (NOT inside checkbox text)
- Keep spacing clean (no broken line rows)
- No extra explanation before or after the table

AFTER TABLE:
Provide exactly 3 concise bullet points under the title:
### Action Strategy
Tailor it for a **creative design student**, focusing on reducing overwhelm and execution clarity.
```

## GitHub Copilot

### Refactor hardware logic

What it does: Tells Copilot to improve a code file by changing how the hardware logic runs, without altering the core setup.

Best for: Fixing slow or blocking code when you want a cleaner, faster version of the same project.

```text
Review the hardware logic across #main.py. The current sensor loop is blocking incoming network packets, causing a delay. Refactor the reading routine to use asynchronous execution (asyncio) so sensor telemetry is queued and sent without pausing the hardware cycle. Keep the hardware pin configurations exactly as they are.
```

### Fix compilation error

What it does: Asks Copilot to look at an error message and repair the related files.

Best for: When your code stops working and you want Copilot to help track down the issue.

```text
The terminal threw a compilation error regarding a missing event loop. Fix this across the files.
```

## Google NotebookLM

### Socratic tutor prompt

What it does: Asks NotebookLM to act like a tutor and quiz you with questions instead of giving away the answers immediately.

Best for: Studying lecture material and checking whether you really understand the topic.

```text
Act as a Socratic tutor. Ask me 3 practice scenario questions based on Chapter 2 of my uploaded slides. Do not reveal the answers until I respond.
```

## Upscayl

### Ultra Sharp (General & Diagrams)

What it does: Enhances edges, sharpens text in diagrams, and recovers fine details in photos and technical assets.

Best for: Screenshots, technical diagrams, flowcharts, and high-detail photos.

```text
Model: REAL-ESRGAN / ULTRA SHARP
Scale: 4x
Image Format: PNG
Double Upscayl: Off (Enable if starting resolution is under 500px)

```

### UltraMix Balanced (Mixed Graphics & CGI)

What it does: Smooths out compression artifacts while preserving textures without adding unwanted noise or over-sharpening halo effects.

Best for: 3D renders, UI mockups, presentation visuals, and composite graphic designs.

```text
Model: ULTRAMIX BALANCED
Scale: 4x
Image Format: PNG
Double Upscayl: Off

```

### Digital Art / Anime (Clean Graphics)

What it does: Sharpens flat colors and vector line work while preventing jagged line edges on solid fills.

Best for: Logos, line art, vector illustrations, and anime-style graphics.

```text
Model: DIGITAL ART / ANIME
Scale: 4x
Image Format: PNG
Double Upscayl: Off

```
---
