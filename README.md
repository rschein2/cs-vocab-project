# CS Vocabulary Project

**Learning systems through spaced repetition**

## The Problem

Learning CS systems (Git, Linux, tmux, Docker, etc.) is a lot like learning a foreign language. The concepts make sense when someone explains them, but if you forget the exact commands, the knowledge fades away. You end up Googling the same commands over and over.

Understanding *why* you'd use `git rebase` vs `git merge` is important. But if you can't remember the actual command when you need it, that understanding becomes useless.

## The Solution

Treat CS systems like vocabulary learning. Use Anki flashcards with:

1. **Practical scenarios** - Not "what does git init do?" but "You want to start tracking a new project. What's the command?"

2. **The WHY, not just the WHAT** - Every card explains why you'd choose this approach, when to use alternatives, and what the flags mean

3. **Deliberate overlap** - The same command appears in multiple scenarios. `git reset` shows up when undoing commits, unstaging files, and recovering from mistakes. This builds pattern recognition.

4. **Command variations** - Each card shows 2-3 related commands or flags, building a web of related knowledge

## The Theory

**Concepts without vocabulary are useless.** You might understand the theory behind rebasing, but if you can't recall the command syntax when you need it, you'll either:
- Google it (breaking flow)
- Avoid using it (limiting your skills)
- Make mistakes (using the wrong flag)

Spaced repetition solves this by building muscle memory. After reviewing these cards, the commands become second nature. You stop thinking "how do I check which files changed?" and just type `git status`.

## How to Use These Cards

### Importing into Anki

1. **Option A - Direct HTML Import:**
   - Open Anki
   - File → Import
   - Select the HTML file
   - Anki will parse the structured cards

2. **Option B - Copy/Paste Individual Cards:**
   - Create a new deck in Anki
   - Add cards manually, copying front and back content
   - Tags are included in each card (cs, git, EN)

3. **Option C - Convert to Anki Package:**
   - Use tools like `genanki` to convert HTML to `.apkg` format
   - Import the package directly

### Study Approach

- **Daily reviews**: 10-15 minutes/day is more effective than cramming
- **Actually type the commands**: When reviewing, type them out (even in thin air). Muscle memory matters.
- **Use them in real projects**: The cards prime your memory, but real usage cements it
- **Be honest with yourself**: If you hesitated or got it wrong, mark it as such. Anki's algorithm works best with honest feedback.

## Card Structure

Each card follows this pattern:

**Front (Question):**
> A practical scenario: "You've made changes to 3 files but only want to commit 2 of them. What's the workflow?"

**Back (Answer):**
- The command(s)
- **Why** you'd use this approach
- 2-3 alternative options or related commands
- Warnings where relevant (e.g., "never rebase shared branches!")

**Tags:** `cs git EN`
- `cs` - Computer Science/Systems topic
- `git` - The specific tool
- `EN` - English language (more languages coming)

## Current Decks

- **git-flashcards.html** - 32 cards covering essential Git workflows
  - Repository basics
  - Staging and committing
  - Branching and merging
  - Rebase vs merge
  - Conflict resolution
  - Remote operations
  - History and searching
  - Recovering from mistakes
  - Tags and releases

## Coming Soon

- Linux command line (ls, grep, find, chmod, etc.)
- tmux (sessions, windows, panes)
- vim (movement, editing, modes)
- Docker (containers, images, volumes)
- SSH and networking
- Shell scripting (bash)
- Build tools (make, cmake)
- Other languages (ES, ZH, FR, DE)

## Contributing

This is an educational resource. If you find errors or want to suggest improvements:
- Commands should be accurate and follow best practices
- Scenarios should be practical and realistic
- Explanations should focus on WHY, not just WHAT
- Include warnings for dangerous operations

## Philosophy

**Memory is the foundation of expertise.** You can't think creatively about Git workflows if you're constantly context-switching to look up basic commands. These cards free up your mental RAM for higher-level problem solving.

The goal isn't to memorize mindlessly - it's to internalize the vocabulary so you can focus on the interesting problems.

---

*Generated for CS students who are tired of Googling the same commands every day.*
