%ifndef era
%include "io.inc"
%endif

section .data
global fix_add_asm

%ifndef era
global main
%endif

section .text

;
; Please enclose all code in main with the %ifndef %endif
; statements!
; This allows all assembler codes to be linkable together
; since this avoids duplicated 'main' symbols.
;
%ifndef era

main:
    ;
    ; You can add stuff to main as well
    ;
    push dword 0
    push dword 6710
    push dword 0
    push dword 134217728
    call fix_add_asm
    add esp, 16
    cmp eax, 134224438
    jne fail1
    cmp edx, 0
    jne fail1
    
    push dword 1561628
    push dword 1073741824
    push dword 233408
    push dword 738197504
    call fix_add_asm      ; call test program
    add esp, 16
    cmp eax, 1811939328
    jne fail2
    cmp edx, 1795036
    jne fail2
    PRINT_STRING "Success"
    ret
    
fail1:
    PRINT_STRING "Wrong result in test 1:"
    NEWLINE
    PRINT_DEC 4, edx
    NEWLINE
    PRINT_DEC 4, eax
    NEWLINE
    PRINT_STRING "Correct result:"
    NEWLINE
    PRINT_STRING "0"
    NEWLINE
    PRINT_STRING "134224438"
    NEWLINE
    ret
    
fail2:
    PRINT_STRING "Wrong result in test 2:"
    NEWLINE
    PRINT_DEC 4, edx
    NEWLINE
    PRINT_DEC 4, eax
    NEWLINE
    PRINT_STRING "Correct result:"
    NEWLINE
    PRINT_STRING "1795036"
    ret
%endif


;
; This is how a possible solution looks like
;
fix_add_asm:
    push ebp
    mov ebp, esp
    push ebx
    mov eax, [ebp + 8]
    mov edx, [ebp + 16]

    add eax, edx

    mov edx, [ebp + 12]
    mov ebx, [ebp + 20]
    adc edx, ebx
    pop ebx
    pop ebp
    ret


