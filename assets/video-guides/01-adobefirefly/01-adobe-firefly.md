# 🎬 Workflow 01: Non-Designer Asset Creator (Adobe Firefly)

This self-contained file serves as the documentation, script index, and workflow guide for **User Story 1: The Non-Designer Asset Creator (Adobe Firefly Lifecycle)** under Project HeyBudi.

---

## 👤 User Story & Target Persona

* **Persona:** Alex, Year 3 student at the School of Engineering (SEG).
* **The Story:**
  > As an engineering student preparing my final year project presentation, I want to generate a clean, customized high-quality presentation backdrop and edit specific visual elements using a text brush without knowing complex graphic software, so that my technical presentation slides look polished and visually elite when graded by the panel.

### 🎯 Objective
Generate a complex engineering visualization from scratch and use Firefly's surgical editing tools (Remove and Expand) to create a presentation-ready 16:9 asset.

### ✅ Acceptance Criteria
- It must allow a non-design student (Alex) to generate a high-quality, professional presentation graphic using simple text prompts via his school-backed 500-credit account.
- It must allow him to easily add or modify specific parts of the image (like inserting an aesthetic tech component icon) using a text-based brush tool (Generative Fill) directly in the web interface.
- It must allow a clean export of the modified image so it can be dropped straight into standard slide builders like PowerPoint or Canva.

---

## 🛠️ Step-by-Step Execution

### Step 1: Base Asset Generation
We will start by generating a complex visualization that might have a few imperfections we want to clean up later.

1. Navigate to **Text to Image** within Adobe Firefly ([firefly.adobe.com](https://firefly.adobe.com)). Ensure you are signed in with your school account.
2. Set **Content Type** to **Photo**.
3. Paste the initial prompt to generate the core engineering concept and click **Generate**:
   
   ```text
   A complex futuristic hydroponics system inside a transparent glass dome, stylized blueprints floating around it, high-tech sensors, clean engineering aesthetic, soft blue and green lighting, corporate visualization style, 8k resolution --ar 16:9
   ```

### Step 2: Surgical Editing (Remove Unwanted Objects)

Often, the generation will include floating text that doesn't make sense, or a sensor that is glitchy. We will remove these seamlessly.

1. Hover over your selected image and click **Edit** ➡️ Select **Generative Fill**.
2. Select the **Remove** tool from the left toolbar.
3. Adjust the brush size and carefully paint over the unwanted elements (e.g., a glitchy sensor, awkward floating text, or a random wire that creates clutter).
4. Leave the prompt bar completely blank (this tells Firefly to just "heal" the area based on the surrounding pixels).
5. Click **Generate**. Firefly will remove the painted elements and fill the void perfectly.
6. Pick the cleanest result and click **Keep**.

### Step 3: Expand and Intelligently Fill the Canvas

Your image is now clean, but perhaps the composition is too tight, leaving no room for presentation text. We will expand the canvas and have the AI intelligently generate more of the environment.

1. Click the **Expand** tool (the crop icon) in the bottom toolkit.
2. Ensure **16:9** is selected.
3. Drag the bounding boxes outward (to the left and right) to create a wider composition.
4. **Optional but Recommended:** Move the existing dome visualization to the right side of the newly expanded canvas. This creates blank space on the left.
5. In the prompt bar, describe what should fill the new empty space, ensuring it matches the original scene, then click **Generate**:

   ```text
   Seamless extension of the clean engineering lab environment, minimalist white desk surface, more subtle geometric blueprint patterns receding into the soft focus background
   ```

6. Firefly will generate the missing parts of the scene, perfectly blending the perspective and lighting of your original dome into the wider environment.
7. Pick the variation that leaves clear space for text and click **Keep**.

### Step 4: Final Export

1. Click **Download** in the top-right corner.
2. The resulting image is now a cohesive, high-resolution 16:9 technical backdrop with clear negative space for your engineering presentation bullet points, built entirely from a single prompt and subsequent edits.

---

## 📹 Video Production Metadata

### Storyboard Outline

1. Open Adobe Firefly by navigating to the home portal
2. Select the Text to Image generator workspace
3. Choose Firefly 5 model and highlight the remaining school generative credit balance
4. Input the base hydroponics concept prompt and execute generation
5. Select the preferred image candidate and load the Edit suite
6. Use the Remove tool from the left sidebar to wipe away clutter
7. Open Generative Expand, stretch to widescreen 16:9, and apply the expansion prompt
8. Export the graphic, drop it straight into a PowerPoint presentation, and activate the AI slide designer tool to map out text areas

### Narration Script

> POV: Your final year project presentation is next week, your engineering project is brilliant, but your slides look completely dead. Stop panicking. Log into Adobe Firefly with your school account and click Text to Image. Switch the model to Firefly 5 for the highest quality. Check your school-backed credits right here, type in your tech background prompt, and hit generate. Find the best image, click edit, and let's customize it. Use the side toolbar, click remove, and brush away any unwanted objects instantly. Next, use generative expand to auto-fill the canvas to a perfect widescreen layout. Hit export, drop that clean graphic straight into PowerPoint, and let AI Designer auto-format your slides. Pop in your title, refresh the designer layout, and you're done.te presentation in under a minute. Work smart, SEG. Follow for more school hacks!"[cite: 1]