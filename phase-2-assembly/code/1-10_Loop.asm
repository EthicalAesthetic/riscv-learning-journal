# ─────────────────────────────────────────────
# Print 1 to 10 using a loop
# RISC-V Assembly — RARS simulator
# ─────────────────────────────────────────────

.data
    newline: .string "\n"      # We'll print this after each number

.text
    main:
        li   t0, 1             # t0 = 1  (our counter, starts at 1)
        li   t1, 10            # t1 = 10 (our limit)

    loop:
        bgt  t0, t1, done      # if t0 > 10, jump to done

        # ── Print the number ──────────────────
        li   a7, 1             # syscall 1 = print integer
        mv   a0, t0            # a0 = t0 (the number to print)
        ecall

        # ── Print a newline ───────────────────
        li   a7, 4             # syscall 4 = print string
        la   a0, newline       # a0 = address of newline string
        ecall

        # ── Increment counter ─────────────────
        addi t0, t0, 1         # t0 = t0 + 1

        j    loop              # jump back to top of loop

    done:
        li   a7, 10            # syscall 10 = exit
        ecall