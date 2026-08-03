# 🤖 HeyBudi: The Democratized AI Framework for NYP Students

[![Target Audience](https://img.shields.io/badge/Audience-NYP%20Students-blue)](https://www.nyp.edu.sg)
[![Framework Status](https://img.shields.io/badge/FYPJ-12%20%20Weeks-orange)](#)

Welcome to **HeyBudi**, an open-source, 12-week Final Year Project (FYPJ) framework designed to bridge the gap between technical and non-technical students across Nanyang Polytechnic (NYP). 

HeyBudi replaces complex, frustrating manual prompt engineering with an open-access repository of pre-written, plug-and-play templates. We empower students across all academic schools (**SIT, SEG, SDM, SBM, SHSS, SAS**) to automate academic administrative friction, build pro-grade assets, and scale everyday productivity using zero-cost or school-backed AI tiers.

[![Troubleshooting Hub](https://img.shields.io/badge/Troubleshooting-Hub-ff6b35?style=for-the-badge)](Troubleshooting-Solutions.md)
[![Prompt Templates](https://img.shields.io/badge/Prompt-Wiki-1f8ef1?style=for-the-badge)](AI-Prompt-Wiki.md)

Need help? Start with the buttons above for a central list of fixes and issue-specific solutions.

---

## 🎯 Core Philosophy

* **Democratized Access (Zero Cost):** Every workflow strictly utilizes free public tiers or school-backed licenses (such as enterprise Microsoft Copilot sandboxes or Adobe student credits) so financial barriers never limit student adoption.
* **Frictionless UX:** Workflows require zero programming. If a student can send a text message, they can leverage a HeyBudi workflow.
* **High-Impact Microlearning:** Built on Cognitive Load Theory principles, delivering immediately actionable technical literacy through rapid, short-form vertical video tutorials.

---

## 🛡️ The Hybrid Pipeline & Workaround
School-provided Microsoft Copilot accounts are securely sandboxed but lack direct OneDrive file and image uploads. HeyBudi introduces a **Hybrid Pipeline** workaround:
1. **Data Security:** Personal, sensitive academic data remains completely sandboxed inside NYP's secure enterprise Microsoft Copilot environment.
2. **Document Analysis:** Anonymous, public free-tier logic engines (ChatGPT, Claude, DeepSeek, Kimi AI) are utilized strictly as public "Document Readers" to process formatting without exposing private info, bypassing Copilot's text-only limitation.

---

## 🧠 Academic & Logic Ecosystem Tools

The core workflows rely on a carefully structured stack of accessible AI capabilities:

* **Microsoft Copilot:** The secure, enterprise-grade core logic engine for student inquiries, document synthesis, and code troubleshooting. Sandboxed accounts ensure absolute student data privacy while preventing external cloud data leak.
* **Adobe Firefly:** A text-to-image creative app used to generate presentation slide backdrops and graphics, allowing non-designer students to bypass creative learning curves using simple text-based "Generative Fill" controls.
* **GitHub Copilot:** An AI pair programmer providing real-time, inline code completions and hardware debugging inside the IDE to accelerate project prototyping for heavy coding modules.
* **Public Free-Tier Engines (ChatGPT / Claude / DeepSeek / Kimi AI):** Utilized strictly as anonymous public "Document Readers" to synthesize layout formatting, convert text into Markdown tables, and translate files, serving as a workaround to bypass sandboxed file-upload limits.
* **Google Ecosystem (Gemini / Google Lens):** Used for Optical Character Recognition (OCR) text extraction, smart note synthesis, and automated calendar syncing to power rapid schedule building.


---

## 🎬 Short-Form Video Series & Core Workflows

Our flagship micro-learning video campaign shows immediate, real-world utility with explicit "Before vs. After" transformations completed in under 60 seconds.

### 📱 Feature Episodes & Playlists

* 🎬 **Episode 1: The Visual Elite**
  * **Focus:** Generating pro-grade presentation backdrops and custom technical assets.
  * **Toolchain:** Adobe Firefly's text-based generative fill.
  * **Watch:** [YouTube Shorts: Episode 1](https://www.youtube.com/shorts/cyMZ1rA7g8A)


* 📅 **Episode 2: The Syllabus Killer**
  * **Focus:** Synthesizing complex course material and research directly in your browser using edge-side web extensions.
  * **Toolchain:** Microsoft Copilot + Microsoft Edge Copilot Extension.
  * **Watch:** [YouTube Shorts: Episode 2](https://youtube.com/shorts/ofPs7ZR9slA?feature=share)


* 💻 **Episode 3: Logic Over Syntax**
  * **Focus:** Programming logic, systems architecture, and code debugging rather than manually typing syntax.
  * **Toolchain:** Microsoft Copilot Sandbox + GitHub Copilot.
  * **Watch:** [YouTube Shorts: Episode 3](https://youtube.com/shorts/ye-KLc_W3oM?feature=share)


* 🚀 **Episode 4: The Instant Study Buddy**
  * **Focus:** Consolidating an entire semester's worth of chaotic lecture notes, PDFs, and slide decks into an interactive personalized study guide and automated audio overview briefings.
  * **Toolchain:** Google NotebookLM.
  * **Watch:** [YouTube Shorts: Episode 4](https://youtube.com/shorts/5z5OgTvg5ew?feature=share)


* 🖼️ **Episode 5: The UpScayl Walkthrough**
  * **Focus:** Enhancing and super-resolving pixelated or low-resolution images locally using open-source neural network models.
  * **Toolchain:** UpScayl (Local AI Image Upscaler).
  * **Watch:** [YouTube Shorts: Episode 5](https://youtube.com/shorts/tQbmySANTgo)


* 🎙️ **Episode 6: Voicebox AI Walkthrough**
  * **Focus:** Instant local voice cloning, speech-to-text transcription, and multi-track audio generation without cloud subscriptions.
  * **Toolchain:** Voicebox AI (Local Open-Source Audio Engine).
  * **Watch:** [YouTube Shorts: Episode 6](https://www.google.com/search?q=https://youtube.com/shorts/lRXrD7s24vw)


* 💬 **Episode 7: The AutoSubs Engine**
  * **Focus:** Transcribing local voiceover audio into dynamic, animated Text+ captions directly inside DaVinci Resolve using open-source offline models.
  * **Toolchain:** AutoSubs (Local DaVinci Resolve Extension) + Parakeet AI Speech Model.
  * **Watch:** [YouTube Shorts: Episode 7](https://youtube.com/shorts/YBCYgfHbZMg?feature=share)

---
### 📈 Production Improvement Notes

These notes track how each episode evolved across the Agile-style production cycle, showing the concrete edits made to improve clarity, pacing, and viewer retention.

* **Episode 1: The Visual Elite / Adobe Firefly**
  * First video produced for the series.
  * Auto subtitles were generated using the Parakeet AI model through the auto-subs workflow.
  * Audio used a generic AI voice track.
  * Cursor tracking was done manually and the result was still rough.
  * Strong as an MVP, but it established the baseline for future production upgrades.

* **Episode 2: The Syllabus Killer / Microsoft Copilot**
  * Editing quality was improved compared to Episode 1.
  * More images were added to the intro to make the opening stronger.
  * A new AI voice clone based on my own voice was added for more natural narration powered by Voicebox Ai with the Qwen TTS 1.7b model.
  * OBS mouse-to-zoom was used for cursor tracking and zoom so viewers could follow the script more easily.
  * MS PowerToys Mouse Highlighter was added to make clicks more visible.

* **Episode 3: Logic Over Syntax / GitHub Copilot**
  * Background music was added to make the video feel more polished.
  * The audio mix still needed refinement, especially for voice EQ and background track leveling.
  * This episode identified the need for better sound balancing in later edits.

* **Episode 4: The Instant Study Buddy / Google NotebookLM**
  * Audio mixing and EQ were improved again.
  * More intro images were added to retain viewer attention for longer.
  * The episode continued the production upgrades introduced in the earlier walkthroughs.

* **Episode 5: The UpScayl Walkthrough**
  * The voice clone was overhauled to sound more energetic and engaging.
  * Voice compression was added to improve clarity and consistency.
  * Audio mixing was refined further for the voice-over and the background music.
  * Technical details were added at the end of the short to keep viewers engaged through the finish.

* **Episode 6: Voicebox AI Walkthrough**
  * Production workflow reached full maturity with highly refined audio generation.
  * Integrated compression and a high-pass filter directly into the Voicebox AI profile.
  * Cleaned up low-frequency mud and balanced voice dynamics at the source, significantly cutting down on post-production audio processing.

* **Episode 7: The AutoSubs Engine / DaVinci Resolve**
  * Closed the post-production pipeline loop by transcribing the Voicebox AI narration locally using the **Parakeet** speech-to-text model inside AutoSubs.
  * Generated word-level aligned `Text+` title blocks directly on Video Track 2 (`V2`) on the DaVinci timeline without relying on cloud credit subscriptions or paid DaVinci Resolve Studio upgrades.
  * Standardized visual asset prompts around a Postman Pat-style claymation aesthetic to boost viewer retention.
  * Designed an open script loop ending (`"So if you are..."`) to seamlessly restart video playback on short-form platforms.

---

## 📁 Repository Navigation

The project files are mapped directly to specific step-by-step documentation guides and resource folders:

```text
├── assets/
│   ├── Images/                       # Visual identity assets (Logos, banners)
│   │   ├── nyp-logo-white-Firefly.png
│   │   └── nyp-logo-white.png
│   ├── prompt-templates.md           # Raw copy-and-paste prompt snippets
│   └── video-guides/                 # Modular step-by-step guides by episode
│       ├── 01-adobefirefly/
│       │   ├── assets/
│       │   └── 01-adobe-firefly.md   # Guide for The Visual Elite (Ep. 1)
│       ├── 02-copilot/
│       │   ├── assets/
│       │   └── 02-edge-copilot.md    # Guide for The Syllabus Killer (Ep. 2)
│       ├── 03-githubcopilot/
│       │   ├── assets/
│       │   └── 03-github-copilot.md  # Guide for Logic Over Syntax (Ep. 3)
│       └── 04-google-notebookLM/
│           ├── assets/
│           └── 04-google-notebookLM.md # Guide for The Instant Study Buddy (Ep. 4)
└── README.md                         # Framework landing page
```

📂 prompt-templates.md: Houses raw copy-and-paste prompt snippets designed for quick clipboard selection.

📂 assets/video-guides: Step-by-step Markdown walkthrough notes corresponding directly to the video tutorials, explaining workflow setup instructions and advanced configurations.


## 🛠️ Post-Production Infrastructure & Toolchain

To maintain zero infrastructure maintenance costs and achieve macro audience retention, this project's content pipeline was built entirely out of cutting-edge local automation, open-source utilities, and advanced AI video tools:

### 🖼️ AI Image Generation

- **Nano Banana Pro**: Used for all AI image generation across the project, including visual assets and supporting graphics.

### 🎬 Video Editing & Composition
* **[DaVinci Resolve & Fairlight Workspace](https://www.blackmagicdesign.com/products/davinciresolve)**: An industry-standard, professional video editing and audio post-production suite used to cut, color grade, and master the series. Elevates project production value to broadcast standards using native dialogue isolation, parametric EQ, and audio ducking scripts.


### 🎙️ Audio Automation & Artificial Intelligence
* **[AutoSubs extension for DaVinci Resolve](https://github.com/tmoroney/auto-subs)**: A timeline extension that runs a self-hosted, local **Parakeet Speech-to-Text model** to generate automated captioning and dynamic text animations, cutting subtitling times by over 85% with 90%+ recognition accuracy.
* **[Voicebox AI](https://github.com/jamiepine/voicebox)**: A high-fidelity, local-first custom voice cloning and synthesis engine that runs completely offline with zero subscription fees, reducing voiceover recording setup and retake overhead by ~80%.
  * Voice settings: Qwen TTS 1.7B AI model with compressor and high-pass filter.

### 🎙️ Recording Equipment Used
* **Microphone:** Behringer Ultravoice XM8500
* **Audio Pre Amp:** Focusrite Scarlett Solo


### 🖥️ UI Capture & Remote Infrastructure
* **[OBS Mouse-to-Zoom Script](https://github.com/BlankSourceCode/obs-zoom-to-mouse)**: Implements dynamic screen zooming and panning that automatically tracks the desktop cursor position in real time. Eliminates 90% of manual video keyframing during editing and keeps mobile viewers focused on small desktop buttons.
  * **Troubleshooting:** [OBS Mouse-to-Zoom troubleshooting notes](Troubleshooting-Solutions.md)
* **[MS PowerToys Mouse Highlighter](https://github.com/microsoft/powertoys)**: Overlays real-time, customizable colored highlighting on mouse clicks. Increases instructional visual focus and viewer comprehension by ~40% for software tutorials.
* **[Parsec Remote Connect (Free Tier)](https://parsec.app/)**: A low-latency, ultra-fast remote networking utility allowing a user to seamlessly connect to, monitor, and run resource-heavy local AI rendering tasks on a powerful home computer right from a basic campus laptop or thin client.

---

## 🤝 Contributing

Are you an NYP student, lecturer, or AI enthusiast with a high-impact, zero-cost workflow to share? 
1. Structure your prompt template in `prompt-templates.md` following our standard format.
2. Open a Pull Request detailing the target student persona and the "Before vs. After" impact metrics!

