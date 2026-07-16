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