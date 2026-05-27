# Contributing to RISC-V Learning Journal

First — thank you for even reading this. This repo is a personal
learning journal, and if you want to contribute to it, that means
you care about open learning and open source. That is exactly the
spirit this project runs on.

**You do not need to be an expert.** Beginners are the most welcome
contributors here. If you spotted something that confused you, there
is a good chance it will confuse others too — fixing it is valuable.

---

## Who should contribute

- Students learning C, RISC-V, embedded systems, or embedded AI
- Anyone who found an error in my notes or code
- Anyone who has a better explanation, resource, or approach
- Anyone who wants to add their own learning notes to a phase folder
- Native Hindi or regional language speakers who want to translate notes

---

## What you can contribute

### Fix something broken or wrong
- Typo or factual error in any `.md` note file
- Bug in a `.c` or `.asm` program
- Incorrect explanation of a concept
- Broken or outdated link to a resource

### Add something useful
- A better example program for a concept already in the notes
- Your own notes on a topic, added as a new file in the right phase folder

### Open an issue
- Something in my notes is unclear or confusing — tell me what
- A concept I should cover that I haven't
- A resource you found useful that I should add
- Anything else that would make this more useful for beginners

---

## How to contribute — step by step

If you are new to GitHub contributions, follow these steps exactly.
It is simpler than it looks.

### Step 1 — Fork this repository
Click the **Fork** button at the top-right of this page. This creates
your own copy of the repo under your GitHub account.

### Step 2 — Clone your fork
```bash
git clone https://github.com/YOUR-USERNAME/riscv-learning-journal.git
cd riscv-learning-journal
```

### Step 3 — Create a branch
Name your branch something descriptive:
```bash
git checkout -b fix/typo-in-phase1-pointers-notes
# or
git checkout -b add/resource-riscv-reader-link
# or
git checkout -b add/hindi-translation-phase1-notes
```

### Step 4 — Make your change
Edit the file. Keep changes focused — one fix or addition per PR.
Do not change unrelated files.

### Step 5 — Commit with a clear message
```bash
git add .
git commit -m "fix: correct pointer explanation in phase-1 notes"
# or
git commit -m "add: K&R C book link to phase-1 resources"
```

Commit message format:
- `fix:` — correcting something wrong
- `add:` — adding new content
- `docs:` — improving documentation
- `translate:` — adding a translation

### Step 6 — Push and open a Pull Request
```bash
git push origin your-branch-name
```
Then go to GitHub, open your fork, and click **"Compare & Pull Request"**.

Write a short description:
- What you changed and why
- Which file(s) you edited
- If fixing a bug: what was wrong, what is correct

---

## Guidelines

- **Be kind.** This is a beginner's repo. Everyone here is learning.
- **One change per PR.** Small, focused PRs get reviewed and merged faster.
- **No plagiarism.** If you reference someone else's explanation, link to the original.
- **In English or Hindi.** Other Indian languages welcome too — create a `lang/` subfolder.
- **Code must run.** If you add a `.c` or `.asm` program, it should compile and run correctly.

---

## Adding your own notes to a phase folder

If you are also learning this material and want to add your own notes:

1. Go to the relevant phase folder (e.g. `phase-1-foundations/notes/`)
2. Create a new file named `your-github-username-topic.md`
   Example: `priya-sharma-pointers.md`
3. Write your notes in that file
4. Open a PR — I will review and merge it

Your notes become part of the shared resource for everyone who finds this repo.

---

## First time contributing to open source?

That is completely fine — this repo is a good place to start. Here is
what the process looks like end to end:

1. You find something to fix or add (check the Issues tab for ideas)
2. You fork, branch, change, commit, push
3. You open a Pull Request
4. I review it (usually within a few days)
5. If it looks good, I merge it — your name appears in the contributors list
6. You have made your first open source contribution

That last step is real. Your GitHub profile will show a contribution
to a RISC-V project. It is a small but genuine start.

---

## Code of conduct

Be respectful. This is a learning space. Condescending, dismissive,
or hostile behavior toward any contributor — especially beginners —
will result in removal from the project.

---

## Questions?

Open an issue with the label `question` and I will answer it.
No question is too basic.

---

*Thank you for contributing. Every fix, every addition, every question
makes this more useful for the next person who finds it.*
