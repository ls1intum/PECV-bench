%ifndef era
%include "io.inc"
%endif

section .data
global fix_sub_asm

%ifndef era
global main
%endif

section .text

;You can add stuff to main as well
%ifndef era
main:
    ;14.5 - 5
    ;push 5
    push 0
    push 335544320
    ;push 14.5
    push 0
    push 973078528
    call fix_sub_asm
    add esp, 16
    ;result in edx:eax
    ret
%endif

;ASSIGNMENT START: fix_sub_asm

fix_sub_asm:
    ret

;ASSIGNMENT END: fix_sub_asm
