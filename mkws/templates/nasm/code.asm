section .text

global _start
_start:
    mov rax, 60
    mov rdx, 0
    syscall
