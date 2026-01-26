;%include "io.inc" <-- Uncomment this for usage in SASM

;--------Do not modify this section--------
section .text
global CMAIN
CMAIN:
;------------------------------------------
    
    ;SASM allows macros like below for easier debugging (uncomment for testing)
    ;Print a string:
    ;PRINT_STRING "Hallo"
    ;----------------------
    ;Print one byte of ecx:
    ;PRINT_DEC 1, ecx
    
    ;To make this compile, add the missing letter below
    add eax, ecx

    ret
