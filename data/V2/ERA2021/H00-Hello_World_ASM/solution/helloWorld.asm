;-------- Do not change this section --------
section .data
    hello db "Hello World!", 10, 0

section .text
global main
extern printf
main:
;--------------------------------------------

    ; Solution: Correct register usage
    add eax, ecx

    push hello
    call printf
    add esp, 4
    ret