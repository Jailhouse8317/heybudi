## Troubleshooting Solutions

### Contents

- [OBS Mouse-to-Zoom](#obs-mouse-to-zoom)
  - [Error: attempt to call field obs_sceneitem_get_info (a nil value)](#error-attempt-to-call-field-obs_sceneitem_get_info-a-nil-value)
- [Voicebox AI](#voicebox-ai)
  - [Fixing Inconsistent or Poor Audio Levels](#fixing-inconsistent-or-poor-audio-levels)

## OBS Mouse-to-Zoom

### Error: `attempt to call field obs_sceneitem_get_info (a nil value)`

This error usually means the OBS Lua script is using older function names that are no longer supported by your OBS version.

### Fix

1. Locate the script file
	- Find the `obs-zoom-to-mouse.lua` file on your computer, such as in your Downloads folder or OBS script directory.

2. Edit the file
	- Open the `.lua` file in a text editor like Notepad.

3. Replace the functions
	- Change all 3 instances of `obs_sceneitem_get_info` to `obs_sceneitem_get_info2`.
	- Change the 1 instance of `obs_sceneitem_set_info` to `obs_sceneitem_set_info2`.

4. Save and reload
	- Save the file.
	- In OBS, go to `Tools > Scripts`.
	- Remove the old script.
	- Add the edited version again.

### Video Guide

If you want a visual walkthrough, watch the guide here:

- [OBS Mouse-to-Zoom Video Guide](https://www.youtube.com/watch?v=0GLLatjfFEE)

### Notes

- This fix is for OBS script compatibility.
- If the error still appears after updating the function names, make sure you are editing the correct copy of the script and not an older duplicate.

## Voicebox AI

### Fixing Inconsistent or Poor Audio Levels

When generating or processing audio in Voicebox AI, audio levels can sometimes sound uneven or muffled. You can resolve these issues directly within your Voice Profile using audio filters.

---

### Which Filter Should You Use?

| Problem | Filter Solution | Why & When to Use |
| :--- | :--- | :--- |
| **Voice levels vary too much** *(e.g., loud spikes mixed with quiet whispers)* | **Compressor Filter** | Smooths out volume inconsistencies by narrowing the dynamic range. It pulls down loud peaks and boosts quiet phrases so the overall output stays balanced and intelligible. |
| **Voice level too low / muffled** *(e.g., weak output, heavy low-end rumble, or mic proximity effect)* | **High-Pass Filter (HPF)** | Cuts low-frequency rumble (typically below 80–100 Hz) that consumes headroom without adding clarity. Removing these unwanted low frequencies allows the core voice range to sit higher and sound clearer in the mix. |

---

### Fix Steps

1. **Open Voice Profile Settings**
   - Navigate to **Voice Profiles** in Voicebox AI.
   - Select the voice profile you want to adjust and click **Edit / Profile Settings**.

2. **Apply Audio Filters**
   - Locate the **Filters / DSP Chain** section for that profile.
   
   - **For Volume Dynamics (Inconsistent Levels):**
     - Add a **Compressor** filter.
     - Set a moderate **Ratio** (e.g., `3:1` to `4:1`).
     - Adjust the **Threshold** so it triggers only during dynamic spikes, and set a slight **Makeup Gain** to restore overall loudness.

   - **For Quiet or Muffled Voice (Low Frequency Build-Up):**
     - Add a **High-Pass Filter** (or **Low-Cut Filter**).
     - Set the frequency cutoff around **80 Hz – 100 Hz**.
     - *(Optional)* If total output is still quiet after filtering low-end mud, apply a clean **Gain** boost.

3. **Save and Test**
   - Save the modified Voice Profile.
   - Run a short sample prompt to verify that levels are consistent and speech clarity is restored.

### Notes

- **Filter Order Matters:** If using both filters together, place the **High-Pass Filter first** to clean up unnecessary low frequencies before sending the clean signal into the **Compressor**.
- Avoid setting the High-Pass cutoff too high (above 120 Hz), as it may make the voice sound thin or metallic.