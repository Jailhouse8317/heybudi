# 🎬 User Story 7: The Local Animated Subtitle Engine (AutoSubs & DaVinci Resolve)

**Persona:** Clarissa / Alex, Year 2 NYP Student (SDM / SIT / SEG)

> **The Story:**  
> As an NYP student editor producing short-form vertical videos for social media and presentations,  
> I want to generate and animate high-engagement `Text+` captions directly on my DaVinci Resolve timeline using the local AutoSubs AI extension,  
> so that I can create punchy, accessible short-form content without paying for a DaVinci Resolve Studio license or uploading my audio clips to cloud subtitle platforms.

---

## 📋 Acceptance Criteria

*   **100% Free & Local Processing:** Must run on the **free version of DaVinci Resolve** using local Whisper AI models via AutoSubs, requiring zero cloud credits or paid Studio upgrades.
*   **Native Text+ Generation:** Must automatically convert transcriptions into dynamic `Text+` title blocks on the timeline, enabling full keyframing, custom fonts, strokes, drop shadows, and pop-in animations.
*   **Short-Form Optimization:** Must allow custom character limits (e.g., 15–20 characters per line) to render high-impact, bite-sized caption blocks ideal for 9:16 vertical content.

---

## 🛠️ Workflow

**Target Persona:** NYP Content Creator / Video Editor  
**Objective:** Transcribe audio locally, generate `Text+` captions, apply high-contrast styling with pop-in animations, and export 9:16 vertical Shorts.

### Step 1: Pre-requisites & Local Installation
1. Go to `tom-moroney.com/auto-subs` or `github.com/tmoroney/auto-subs`.
2. Download and run the standalone installer for **Windows (`.exe`)** or **macOS (`.pkg`)**.
3. Ensure **DaVinci Resolve** was installed directly from Blackmagic Design's official website for script integration.

### Step 2: Set Up 9:16 Vertical Timeline
1. Launch **DaVinci Resolve** → Open **Timeline Settings**.
2. Set resolution to **Custom**: **1080 x 1920** (Check **Use vertical resolution**).
3. Import your video clip or voiceover track onto Audio Track 1 (`A1`).

### Step 3: Run AutoSubs Integration Script
1. Go to **Workspace** → **Scripts** → **AutoSubs** inside Resolve.
2. Select **Whisper Small** or **Whisper Medium** for optimal speed and accuracy.
3. Set max characters per line to **15–20 characters** for punchy 2–4 word subtitle blocks.
4. Click **Transcribe** → Click **Send to Resolve** to output editable `Text+` titles on Video Track 2 (`V2`).

### Step 4: Styling & Animation (`Text+`)
1. Highlight a `Text+` clip → Open the **Inspector** panel.
2. **Font & Color:** Choose bold fonts (*Impact*, *Montserrat*, *Inter*) in high-contrast White or Neon Yellow (`#FFFF00`).
3. **Stroke & Shadow:** Under **Shading**, enable a black stroke outline and drop shadow for maximum legibility.
4. **Pop-in Effect:** Keyframe the scale/zoom (e.g., 0.8 to 1.0 over 3 frames) or apply a preset zoom macro.
5. **Paste Attributes:** Copy the styled title block, select all remaining subtitle clips on `V2`, right-click → **Paste Attributes** → Check **Text+ Parameters**.

---

## 🎙️ Video Voiceover Script

> Exhausted from manually typing out subtitles line-by-line for your videos?
> 
> **STOP scrolling!**
> 
> Don't waste money upgrading to paid software just for auto-captions. Here is how to generate animated subtitles for free!
> 
> 1. Head over to [tom-moroney.com/auto-subs](https://tom-moroney.com/auto-subs/), click download, and run the setup file to install it on your PC.
> 2. Open the AutoSubs app. You'll see it isn't connected to your editor yet, so close it and launch **DaVinci Resolve**!
> 3. Open your video project, click **Scripts** from the top menu, and launch AutoSubs directly inside DaVinci! Now it's connected!
> 4. Select your audio track, pick the Parakeet AI model for English, and leave the language on English.
> 5. Hit **Generate**! Watch the AI transcribe your speech and automatically line up the word-level timing.
> 6. Review the text and click **Add to Timeline**...
> 
> AutoSubs is a completely free, open-source tool—meaning all transcription runs strictly locally on your PC with zero cloud uploads!
> 
> Work smart! Save this video and try it today!