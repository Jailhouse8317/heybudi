## User Story 3: The Non-Programmer Logic Assistant

### GitHub Copilot Lifecycle

**Persona:** Alex, Year 3 student at the School of Engineering (SEG).

> **The Story:**
> * "As an engineering student who needs to write complex hardware-programming logic for my technical project,"
> * "I want an inline AI assistant to predict my hardware code blocks and securely explain syntax errors right inside my code editor,"
> * "So that I can successfully compile my engineering prototype without getting stuck for days on unfamiliar programming code."
> 
> 

---

### 📋 Acceptance Criteria

What your solution must do:

* **Real-Time Inline Predictions:** Provide real-time, greyed-out inline code predictions (e.g., Arduino C++ or Python loops) inside Alex's IDE (like VS Code) based on the hardware components he is trying to program.
* **Interactive Chat Panel:** Feature an inline chat panel that allows him to highlight a broken block of engineering logic, get an immediate plain-English explanation of the bug, and receive a secure refactor fix.
* **Secure Academic Tier:** Fully activate using the free **GitHub Education Student Admin Card** verification tier, ensuring his academic project data remains securely sandboxed.

---

### 🎯 Target & Objective

* **Target Persona:** Alex (SEG)
* **Objective:** Leverage **GitHub Copilot’s Agent Mode (Copilot Edits)** within VS Code to refine complex, multi-file hardware-programming logic (e.g., Python IoT gateways or Arduino C++ device routines), diagnose compilation bugs, and safely refactor hardware logic entirely inside the workspace.

---

## 🛠️ Prerequisites & Verification (Zero-Cost & Secure)

1. **Setup Extensions:** Open **VS Code** and ensure the **GitHub Copilot** and **GitHub Copilot Chat** extensions are installed.
2. **Academic Authentication:** Sign in to your GitHub account. Ensure your account is verified under the **GitHub Education Student Developer Pack** (your free academic tier).
3. **Data Security Sandbox:** Because this is verified via an academic tier, your local engineering project files and proprietary hardware layouts remain secure and sandboxed within your workspace session.

---

## 🚀 Step-by-Step Execution

### Step 1: Triggering the Autonomous Agent Mode (Copilot Edits)

Instead of asking questions in a separate chat sidebar and copying code back and forth, Alex will use Copilot Edits to let the AI agent work *directly* on his open files.

1. Open your hardware project folder in **VS Code**.
2. Open the **Copilot Edits** view (click the secondary sidebar icon or press `Ctrl+Shift+I` / `Cmd+Shift+I`).
3. Click the **"Add Files"** button (or type `#`) to select the exact files that form your hardware logic working set (e.g., `sensor_reading.py`, `mqtt_gateway.py`, or `main.ino`).
4. Switch the session from standard chat to **Agent Mode** using the mode toggle in the panel.

### Step 2: Delegating High-Level Logic Refactoring

Alex has written a functional block of code, but it is unoptimized, blocks the main execution loop, or drops sensor packets. He wants to refine it without manually rewriting arrays or thread loops.

1. In the Copilot Edits prompt bar, dictate a high-level architectural instruction instead of writing raw code blocks:
> **Prompt:** "Review the hardware logic across `#main.py`. The current sensor loop is blocking incoming network packets, causing a delay. Refactor the reading routine to use asynchronous execution (asyncio) so sensor telemetry is queued and sent without pausing the hardware cycle. Keep the hardware pin configurations exactly as they are."


2. Press `Enter`.
3. **The Agent Action:** Copilot will act as an agent—it scans your workspace dependencies, plans a multi-file structural edit, and updates the targeted files simultaneously.

### Step 3: Reviewing and Testing the Agent's Diffs

1. **Inspect Changes:** As Copilot edits your code, you will see a live summary of modified files and an inline code diff layout within your editor window.
2. **Review Diffs:** Click into a modified file to view the changes side by side:
* **Green highlights:** Optimization fixes.
* **Red highlights:** Removed bottlenecks.


3. **Run Code:** Open your integrated VS Code terminal and compile or run your hardware environment script.
4. **Self-Correction Loop:** *If a Compilation Error Occurs*, you don't need to debug it manually. Simply type in the Edits panel:
> **Prompt:** "The terminal threw a compilation error regarding a missing event loop. Fix this across the files."


5. Copilot’s agentic loop will read the runtime error, self-correct its own code proposal, and re-apply a clean patch to your files.

### Step 4: Accepting the Workspace Refactor

1. Once the terminal compiles successfully and the logic is smooth, finalize the changes.
2. In the Copilot Edits bar, click the **"Accept"** button (or press `Tab` on individual code chunks) to merge the optimized logic permanently into your workspace.
3. **Safety Net:** If an approach doesn't work out as intended, click **"Undo/Reset"** to instantly revert all modified files back to your original baseline state without losing any data.