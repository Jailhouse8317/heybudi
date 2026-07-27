## 🎙️ User Story 6: The AI Voice Cloner & Audio Stylist (Voicebox AI Lifecycle)

**Persona:** Clarissa / Alex, Year 2 NYP Student (SIT / SEG / SBM)

**The Story:** > As an NYP student producing short-form educational and promotional videos,

> I want to clone my own voice locally and process the audio with built-in compressor and high-pass filter settings using Voicebox AI,
> 
> 
> so that I can generate realistic, high-quality narrations for my video scripts in seconds without paying for cloud subscriptions or compromising my voice privacy.
> 

### 📋 Acceptance Criteria (What your solution must do)

- **100% Local & Privacy-First Execution:** It must run entirely on the student's local laptop/PC via Voicebox AI with zero cloud uploads, ensuring personal voice data remains 100% private.
- **Zero-Cost Voice Cloning & Generation:** It must allow the student to clone a target voice using a short, clean audio reference clip (5–10 seconds) and generate realistic TTS voiceovers without subscription limits or credit tiers.
- **Built-In Audio Processing & Filtering:** It must support audio post-processing (high-pass filter and compressor settings) to remove low-frequency mic rumble and produce production-ready, clear voice tracks for video editors.
- **Seamless Audio Export:** It must allow quick audio exports in high-quality WAV/MP3 format, ready to be dropped into editing software like CapCut or DaVinci Resolve.

### 🛠️ Workflow: Self-Hosted Voicebox AI Voice Cloning & Audio Synthesis

**Target Persona:** NYP Student / Content Creator

**Objective:** Clone your voice locally, generate a timed short-form video narration script, apply high-pass and compressor audio filters, and export high-fidelity audio for video editing.

#### Step 1: Install & Launch Voicebox AI (Zero-Cost Setup)

- Navigate to voicebox.sh and download the installer for your operating system (Windows / macOS).
- Run the installer wizard and launch the Voicebox AI desktop application.
- *Note:* The local engine starts automatically on `localhost:17493` with zero external API key requirements.

#### Step 2: Create Your Voice Profile (Voice Cloning)

- Open the **Voice Profiles** tab in Voicebox AI and click **Create Profile / Clone Voice**.
- Upload or record a clean, noise-free **5 to 10-second reference audio sample** of your voice (recorded in mono/stereo using an onboard or USB mic).
- Name your profile (e.g., `NYP_Student_Voice`). Voicebox will automatically process the reference clip via its local TTS engine (e.g., Qwen3-TTS / Chatterbox).

#### Step 3: Script Ingestion & Audio Generation

- Paste your target short-form script into the generation text area.

<aside>
7️⃣

"If you're an IT student drowning in MASSIVE module plans, lab timelines, and endless project documentation... STOP scrolling!"

"Your school IT policy blocks external file uploads to public AI tools, right?! But you STILL need to parse a sixteen week roadmap."

</aside>

- Select your cloned voice profile from the dropdown menu.
- Click **Generate** to render the speech locally on your GPU/CPU.

#### Step 4: Apply Post-Processing Effects (Compressor & High-Pass Filter)

- Navigate to the **Effects / Post-Processing** panel in Voicebox.
- **High-Pass Filter:** Set the cut-off frequency to **80 Hz – 100 Hz** to eliminate background hum and low-end room rumble.
- **Compressor Settings:**
    - *Threshold:* `18 dB` to `20 dB`
    - *Ratio:* `3:1` or `4:1` (for consistent vocal dynamics)
    - *Attack:* `15 ms` | *Release:* `100 ms`
- Apply the effect chain to polish the vocal track to broadcast quality.

#### Step 5: Export & Integration

- Preview the master audio file using the built-in player.
- Click **Export / Download** to save the polished `.wav` file to your local workspace folder.
- Import the audio file directly into your video timeline (CapCut or DaVinci Resolve) to match your visual edits.