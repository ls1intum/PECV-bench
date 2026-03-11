%ifndef era
%include "io.inc"
%endif
section .bss
    v1: resd 6
    v2: resd 6
    o: resd 6
section .data
global fix_vec_cross_asm
extern fix_mul_asm

%ifndef era
global main
%endif

section .text

;You can add stuff to main as well
%ifndef era
main:
    ; write your own test code here
    ; missing: set values in v1
    ; missing: set values in v2
    push dword o
    push dword v2
    push dword v1
    call fix_vec_cross_asm
    add esp, 12
    ;o = v1 x v2
    ret
%endif

;ASSIGNMENT START: fix_vec_cross

fix_vec_cross_asm:
    ret


;ASSIGNMENT END: fix_vec_cross

