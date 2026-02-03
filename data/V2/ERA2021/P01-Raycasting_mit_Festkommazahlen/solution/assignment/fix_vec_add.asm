%ifndef era
%include "io.inc"
%endif
section .bss
    v1: resd 6
    v2: resd 6
    o: resd 6

section .data
global fix_vec_add_asm

%ifndef era
global main
%endif

section .text

;You can add stuff to main as well
%ifndef era
main:
    ;set v1
    mov dword [v1], 67108864
    mov dword [v1+4], 0
    mov dword [v1+8], 67108864
    mov dword [v1+12], 0
    mov dword [v1+16], 67108864
    mov dword [v1+20], 0
    ;set v2
    mov dword [v2], 4227858432
    mov dword [v2+4], 4294967295
    mov dword [v2+8], 4227858432
    mov dword [v2+12], 4294967295
    mov dword [v2+16], 4227858432
    mov dword [v2+20], 4294967295
    push dword o
    push dword v2
    push dword v1
    call fix_vec_add_asm
    add esp, 12
    cmp dword [o],0
    jne fail
    cmp dword [o+4], 0
    jne fail
    cmp dword [o+8],0
    jne fail
    cmp dword [o+12], 0
    jne fail
    cmp dword [o+16],0
    jne fail
    cmp dword [o+20], 0
    jne fail
    PRINT_STRING "Success"
    ret
    fail:
    PRINT_STRING "Test failed"
    ret
%endif

;ASSIGNMENT START: fix_vec_add

fix_vec_add_asm:
    ret

;ASSIGNMENT END: fix_vec_add

