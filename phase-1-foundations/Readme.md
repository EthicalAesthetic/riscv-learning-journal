# Phase 1 — Foundations (C Programming & Computer Architecture)

[![Phase](https://img.shields.io/badge/Phase-1%20of%206-teal?style=flat-square)](../README.md)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)](#weekly-progress-log)
[![Focus](https://img.shields.io/badge/Focus-C%20%26%20Architecture-blueviolet?style=flat-square)](#what-phase-1-covers)

> I started this phase knowing basic C from university — `printf`, loops, functions.
> That's surface-level C. Embedded systems demand something deeper: you need to understand
> memory at the address level, manipulate bits to talk to hardware registers, and know
> what a processor is actually doing when your code runs. Phase 1 fixes the gap.
> Everything that comes later in RISC-V work builds on what's here.

---

## What Phase 1 covers

Two tracks, running in parallel:

- **1A — C Programming for Embedded Systems** (Weeks 1–8): Relearning C the way hardware actually uses it — pointers, memory, bit manipulation, low-level I/O.
- **1B — Computer Architecture Basics** (Weeks 1–8): Understanding what a processor is and how it executes code.

You don't finish 1A before starting 1B. They feed each other.

---

## 1A — C Programming for Embedded Systems

Embedded C teaches you to write programs that *talk to hardware*. Includes talking to registers, bit manipulation, memory-mapped I/O, and understanding why `volatile` exists.

### Resources

| Resource | What it covers | Access |
|---|---|---|
| *The C Programming Language* — Kernighan & Ritchie (K&R) | The original. Pointers, arrays, memory management. Do every exercise. | Free PDF online |
| *Programming Embedded Systems in C and C++* — Michael Barr | Registers, bit manipulation, memory-mapped I/O, interrupts — the actual embedded C toolkit | Free PDF / O'Reilly |
| CS50x — Harvard / edX | Weeks 1–4 only: C fundamentals, arrays, memory. Use this if the foundation feels shaky | Free / edX |


## Practice Exercises

These are not exercises for exercise's sake — each one is a concrete embedded systems skill.

**Bit Manipulation**
- [ ] Write a C program that uses `AND`, `OR`, `XOR`, and shift operators on a variable — this is how you control hardware registers

**Memory & Pointers**
- [ ] Write a program using `malloc()` and `free()` — print pointer addresses to the console, understand what you're actually seeing

**Low-Level I/O**
- [ ] Write a C program that reads from and writes to a file using `open()` / `read()` / `write()` system calls — not `printf` / `scanf` — this is how peripheral communication works

**Linked List**
- [ ] Implement a simple linked list from scratch — the point is not data structures, it's pointer manipulation and dynamic memory

---

## 1B — Computer Architecture Basics

You cannot write meaningful RISC-V code without knowing what happens between the moment your code is compiled and the moment the processor executes it. This track takes you inside the machine.

### Resources

| Resource | What it covers | Access |
|---|---|---|
| *Computer Organization and Design: RISC-V Edition* — Patterson & Hennessy | The foundational textbook. Written by RISC-V's creators. Read Chapters 1–4 in Phase 1. | Free PDF widely available |
| CS61C — UC Berkeley | The Berkeley course where RISC-V was born. All lectures on YouTube. Uses Patterson & Hennessy. | Free / YouTube |

> 💡 **Key Insight:** Patterson & Hennessy didn't just write about RISC-V — they created it. Reading this book is learning architecture from its source. Chapters 1–4 alone, done seriously, will put you ahead of most people who casually claim RISC-V knowledge. (From Reading Book, I mean using NotebookLM)

### Book Chapters — Phase 1 Scope

- [ ] Chapter 1 — Computer Abstractions and Technology
- [ ] Chapter 2 — Instructions: Language of the Computer
- [ ] Chapter 3 — Arithmetic for Computers
- [ ] Chapter 4 — The Processor

---

## Self-Assessment Checklist

These are the concepts I should be able to explain out loud — without notes — by the time Phase 1 is done. If I can't explain it clearly, I don't actually understand it yet.

- [ ] What is an instruction? What is machine code? What is assembly language?
- [ ] What is the fetch-decode-execute cycle?
- [ ] What are registers? Why does a CPU use registers instead of just reading from RAM every time?
- [ ] What is the difference between the stack and the heap in memory?
- [ ] What happens at the assembly level during a function call? (Stack frame, return address, saved registers.)
- [ ] What is memory-mapped I/O?

> Check a box only when you can explain it to someone else, not just when you've read about it.

---

## Topics covered in Phase 1

### 1. C programming fundamentals
- Variables, data types, operators
- Control flow — if, for, while, switch
- Functions — declaration, definition, return values
- Arrays and strings
- `printf` and `scanf`

### 2. Pointers and memory
- What a pointer is — an address, not a value
- Pointer arithmetic
- Passing by value vs passing by reference
- `malloc()` and `free()` — heap allocation
- Common pointer bugs — null dereference, dangling pointer, memory leak
- How to print a memory address using `%p`

### 3. Functions and the call stack
- What happens in memory when you call a function
- Stack frame — local variables, return address, saved registers
- Recursive functions and stack depth
- Why stack overflow happens

### 4. Bit manipulation
- AND `&`, OR `|`, XOR `^`, NOT `~`
- Left shift `<<` and right shift `>>`
- Setting, clearing, toggling individual bits
- Why embedded systems use bit manipulation to control hardware registers

### 5. Computer architecture basics
- Von Neumann architecture — CPU, memory, I/O
- What an instruction is
- Registers vs RAM — speed and size tradeoffs
- The fetch-decode-execute cycle
- What an ISA (Instruction Set Architecture) is
- Why RISC (Reduced Instruction Set) vs CISC matters



## Folder structure

```
phase-1-foundations/
├── README.md          ← you are here
├── notes/             # personal notes — C, architecture, concepts
└── code/              # practice C programs from the 1A exercises
```

---

## How to compile and run any C file here

```bash
# compile
gcc filename.c -o output -Wall

# run
./output

# compile with debug info (useful with gdb)
gcc filename.c -o output -g -Wall
```

`-Wall` enables all warnings. Always compile with `-Wall` — warnings are
bugs waiting to happen, especially with pointers.

---

## Notes for contributors

If you are also going through Phase 1 and want to add your notes or
a better version of any exercise:

1. Add your notes file as `notes/your-github-username-topic.md`
2. Add your code file as `code/your-github-username-exercise.c`
3. Make sure your C code compiles cleanly with `gcc -Wall`
4. Open a PR — see [CONTRIBUTING.md](../CONTRIBUTING.md)

