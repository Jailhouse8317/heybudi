# 🤖 HeyBudi: The Democratized AI Framework for NYP Students

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Target Audience](https://img.shields.io/badge/Audience-NYP%20Students-blue)](https://www.nyp.edu.sg)
[![Framework Status](https://img.shields.io/badge/FYPJ-Week%207%20(Production)-orange)](#)

Welcome to **HeyBudi**, an open-source, 12-week Final Year Project (FYPJ) framework designed to bridge the gap between technical and non-technical students across Nanyang Polytechnic (NYP). 

HeyBudi replaces complex, frustrating manual prompt engineering with an open-access repository of pre-written, plug-and-play templates. We empower students across all academic schools (**SIT, SEG, SDM, SBM, SHSS, SAS**) to automate academic administrative friction, build pro-grade assets, and scale everyday productivity using zero-cost or school-backed AI tiers.

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
* **Perplexity / Manus AI:** Autonomous, agent-based deep research engines that navigate multiple web source tabs to gather live information and compile structured presentation outlines.

---

## 🎬 Short-Form Video Series & Core Workflows

Our flagship micro-learning video campaign shows immediate, real-world utility with explicit "Before vs. After" transformations completed in under 60 seconds.

### 📱 Feature Episodes & Playlists

* 🎬 **Episode 1: The Visual Elite** 
  * **Focus:** Generating pro-grade presentation backdrops and custom technical assets.
  * **Toolchain:** Adobe Firefly's text-based generative fill.
  * **Watch:** [YouTube Shorts: Episode 1](https://www.youtube.com/shorts/cyMZ1rA7g8A)
* 📅 **Episode 2: The Syllabus Killer** 
  * **Focus:** Converting a messy, dense syllabus screenshot into a structured, dynamic assignment timeline.
  * **Toolchain:** Google Lens (OCR) + Markdown Logic Engines.
  * **Watch:** [YouTube Shorts: Episode 2](https://youtube.com/shorts/ofPs7ZR9slA?feature=share)
* 💻 **Episode 3: Logic Over Syntax** 
  * **Focus:** Programming logic, systems architecture, and code debugging rather than manually typing syntax.
  * **Toolchain:** Microsoft Copilot Sandbox + GitHub Copilot.
  * **Watch:** [YouTube Shorts: Episode 3](https://youtube.com/shorts/ye-KLc_W3oM?feature=share)
* 🚀 **Episode 4: The Instant Study Buddy** 
  * **Focus:** Consolidating an entire semester's worth of chaotic lecture notes, PDFs, and slide decks into an interactive personalized study guide and automated audio overview briefings.
  * **Toolchain:** Google NotebookLM.
  * **Watch:** [YouTube Shorts: Episode 4 Preview](https://youtube.com/shorts/5z5OgTvg5ew?feature=share)

---

## 📁 Repository Navigation

The project files are mapped directly to specific step-by-step documentation guides and resource folders:

```text
├── assets/
│   ├── Images/                       # Visual identity assets (Logos, banners)
│   │   ├── nyp-logo-white-Firefly.png
│   │   └── nyp-logo-white.png
│   ├── prompt-templates/             # Raw copy-and-paste prompt snippets
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

📂 assets/prompt-templates: Houses raw copy-and-paste prompt snippets designed for quick clipboard selection.

📂 assets/video-guides: Step-by-step Markdown walkthrough notes corresponding directly to the video tutorials, explaining workflow setup instructions and advanced configurations.


## 🛠️ Post-Production Infrastructure & Toolchain

To maintain zero infrastructure maintenance costs and achieve macro audience retention, this project's content pipeline was built entirely out of cutting-edge local automation, open-source utilities, and advanced AI video tools:

### 🎬 Video Editing & Composition
* **[DaVinci Resolve & Fairlight Workspace](https://www.blackmagicdesign.com/products/davinciresolve)**: An industry-standard, professional video editing and audio post-production suite used to cut, color grade, and master the series. Elevates project production value to broadcast standards using native dialogue isolation, parametric EQ, and audio ducking scripts.


### 🎙️ Audio Automation & Artificial Intelligence
* **[AutoSubs extension for DaVinci Resolve](https://github.com/tmoroney/auto-subs)**: A timeline extension that runs a self-hosted, local **Parakeet Speech-to-Text model** to generate automated captioning and dynamic text animations, cutting subtitling times by over 85% with 90%+ recognition accuracy.
* **[Voicebox AI](https://voicebox.sh/download)**: A high-fidelity, local-first custom voice cloning and synthesis engine that runs completely offline with zero subscription fees, reducing voiceover recording setup and retake overhead by ~80%.


### 🖥️ UI Capture & Remote Infrastructure
* **[OBS Mouse-to-Zoom Script](https://github.com/BlankSourceCode/obs-zoom-to-mouse)**: Implements dynamic screen zooming and panning that automatically tracks the desktop cursor position in real time. Eliminates 90% of manual video keyframing during editing and keeps mobile viewers focused on small desktop buttons.
* **[MS PowerToys Mouse Highlighter](https://github.com/microsoft/powertoys)**: Overlays real-time, customizable colored highlighting on mouse clicks. Increases instructional visual focus and viewer comprehension by ~40% for software tutorials.
* **[Parsec Remote Connect](https://parsec.app/)**: A low-latency, ultra-fast remote networking utility allowing a user to seamlessly connect to, monitor, and run resource-heavy local AI rendering tasks on a powerful home computer right from a basic campus laptop or thin client.

---

## 🤝 Contributing

Are you an NYP student, lecturer, or AI enthusiast with a high-impact, zero-cost workflow to share? 
1. Fork this repository.
2. Structure your prompt template inside the `/prompts` directory following our standard format.
3. Open a Pull Request detailing the target student persona and the "Before vs. After" impact metrics!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.