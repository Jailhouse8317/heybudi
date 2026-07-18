## Troubleshooting Solutions

### Contents

- [OBS Mouse-to-Zoom](#obs-mouse-to-zoom)
  - [Error: attempt to call field obs_sceneitem_get_info (a nil value)](#error-attempt-to-call-field-obs_sceneitem_get_info-a-nil-value)

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
