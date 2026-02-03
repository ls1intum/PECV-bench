%ifndef era
%include "io.inc"
%endif

section .data
global fix_mul_asm

%ifndef era
global main
%endif

section .text

;You can add stuff to main as well
%ifndef era
main:
    ;calculate 13 * 2.5
    ;push 2.5
    push 0
    push 167772160
    ;push 13
    push 0
    push 872415232
    call fix_mul_asm
    add esp, 16
    ;value in edx:eax
    ;...do other stuff
    ret
%endif

;ASSIGNMENT START: fix_mul_asm
fix_mul_asm:
    ; You can also develop other functions/subprograms in here
    ret

;ASSIGNMENT END: fix_mul_asm
