## User Story 1: The Non-Designer Asset Creator (Adobe Firefly Lifecycle)

**Persona:** Alex, Year 3 student at the School of Engineering (SEG).

**The Story:** > As an engineering student preparing my final year project presentation,

> I want to generate a clean, customized high-quality presentation backdrop and edit specific visual elements using a text brush without knowing complex graphic software,
so that my technical presentation slides look polished and visually elite when graded by the panel.
> 

**Acceptance Criteria (What your solution must do):**

- It must allow a non-design student (Alex) to generate a high-quality, professional presentation graphic using simple text prompts via his school-backed 500-credit account.
- It must allow him to easily add or modify specific parts of the image (like inserting an aesthetic tech component icon) using a text-based brush tool (Generative Fill) directly in the web interface.
- It must allow a clean export of the modified image so it can be dropped straight into standard slide builders like PowerPoint or Canva.



**Target Persona:** Alex (SEG)

**Objective:** Generate a complex engineering visualization from scratch and use Firefly's surgical editing tools (Remove and Expand) to create a presentation-ready 16:9 asset.

## Step-by-Step Execution

### Step 1: Base Asset Generation

We will start by generating a complex visualization that might have a few imperfections we want to clean up later.

1. Navigate to **Text to Image** within Adobe Firefly (firefly.adobe.com). Ensure you are signed in with your school account.
2. Paste the initial prompt to generate the core engineering concept:
    
    > `"A complex futuristic hydroponics system inside a transparent glass dome, stylized blueprints floating around it, high-tech sensors, clean engineering aesthetic, soft blue and green lighting, corporate visualization style, 8k resolution --ar 16:9"`
    > 
3. Set **Content Type** to **Photo**.
4. Click **Generate**.

### Step 2: Surgical Editing (Remove Unwanted Objects)

Often, the generation will include floating text that doesn't make sense, or a sensor that is glitchy. We will remove these seamlessly.

1. Hover over your selected image and click **Edit** -> Select **Generative Fill**.
2. Select the **Remove** tool from the left toolbar.
3. Adjust the brush size and carefully paint over the unwanted elements (e.g., a glitchy sensor, awkward floating text, or a random wire that creates clutter).
4. Leave the prompt bar *completely blank* (this tells Firefly to just "heal" the area based on the surrounding pixels).
5. Click **Generate**. Firefly will remove the painted elements and fill the void perfectly. Pick the cleanest result and click **Keep**.

### Step 3: Expand and Intelligently Fill the Canvas

Your image is now clean, but perhaps the composition is too tight, leaving no room for presentation text. We will expand the canvas and have the AI intelligently generate *more* of the environment.

1. Click the **Expand** tool (the crop icon) in the bottom toolkit.
2. Ensure **16:9** is selected. Drag the bounding boxes *outward* (to the left and right) to create a wider composition.
3. *Optional but Recommended:* Move the existing dome visualization to the right side of the newly expanded canvas. This creates blank space on the left.
4. In the prompt bar, describe what should fill the new empty space, ensuring it matches the original scene:
    
    > `"Seamless extension of the clean engineering lab environment, minimalist white desk surface, more subtle geometric blueprint patterns receding into the soft focus background"`
    > 
5. Click **Generate**.
6. Firefly will generate the missing parts of the scene, perfectly blending the perspective and lighting of your original dome into the wider environment. Pick the variation that leaves clear space for text and click **Keep**.

### Step 4: Final Export

1. Click **Download** in the top-right corner.
2. The resulting image is now a cohesive, high-resolution 16:9 technical backdrop with clear negative space for your engineering presentation bullet points, built entirely from a single prompt and subsequent edits.

