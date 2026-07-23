## User Story 2: The Non-Technical Workflow Builder (Microsoft Copilot Lifecycle)

**Persona:** Priya, Year 2 student at the School of Infocomm & Technology (SIT).

> **The Story:**
> As an IT student who feels overwhelmed by administrative logistics and text-heavy guidelines,
> I want to use my browser's built-in AI sidebar to read active text documents and instantly organize them into a step-by-step checklist, so that I can manage my project milestones without getting bogged down by my school account's lack of file upload features.

**Acceptance Criteria (What your solution must do):**

* It must use Microsoft Edge Copilot's page context to analyze open web documents or raw text layouts without requiring an attachment upload.
* It must automatically extract dates, deliverables, and weightage, sorting them into a structured Markdown table.
* It must allow Priya to copy-paste the output table directly into an external workspace dashboard like Notion without breaking the cell formatting.

---

# Workflow Guide: Multi-Tab Project Synthesis with Edge Copilot

**Target Persona:** Priya (SDM)

**Objective:** Cross-reference an assignment brief and a grading rubric across active browser tabs to generate an automated project checklist and milestone timeline—all without uploading files.

## Prerequisites & Setup

1. Open **Microsoft Edge**.
2. Log into your school Microsoft account (if applicable, to ensure data privacy/higher limits), though the standard tier works perfectly.
3. Open the following tabs in your browser window:
* **Tab 1:** Your SDM Assignment Brief (e.g., a PDF opened in Edge, a Brightspace page, or a Canvas module).
* **Tab 2:** The project’s Assessment Rubric/Grading Criteria.


4. Click the **Copilot icon** (the blue speech bubble) in the top-right corner of Edge to open the AI sidebar.
5. **Crucial Step:** Click the triple dots (`...`) at the top of the Copilot sidebar, go to **Notification and App settings**, and ensure **"Allow Microsoft to access page content"** is turned **ON**.

---

## Step-by-Step Execution

### Step 1: Prime the Context

Before asking for the final table, you need to ensure Copilot is actively reading both tabs.

**Paste this prompt into the Edge Copilot sidebar:**

> I have opened my SDM Assignment Brief in Tab 1 and the Assessment Rubric in Tab 2. Please scan the content of both active tabs. Acknowledge if you can read them by replying with "Ready", and summarize the main objective of the assignment in one sentence.

### Step 2: Extract & Synthesize (The Core Prompt)

Once Copilot replies with "Ready", use this highly structured prompt to extract the data and format it perfectly for Notion.

**Paste this prompt next:**

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

### Step 3: Verifying the Output

Copilot will output a clean Markdown table. Before moving to Notion, Priya should double-check:

* Are the weightages (e.g., *Final Prototype - 40%*) matching the rubric tab?
* Are the milestones broken down sequentially?

---

## Transferring to Notion (Hassle-Free Copy)

Because Edge Copilot outputs native Markdown, moving this to Notion without breaking cells is incredibly simple:

1. Hover over the top-right corner of Copilot's response box and click the **"Copy"** icon (or highlight the table and press `Ctrl+C` / `Cmd+C`).
2. Open your Notion workspace dashboard page.
3. Click into an empty block and press **`Ctrl+V`** (or `Cmd+V`).
4. **Result:** Notion automatically recognizes the Markdown table syntax and instantly converts it into a clean, fully formatted, editable **Notion Table block** with columns and rows perfectly intact.