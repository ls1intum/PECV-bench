;-------- Do not change this section --------
section .data
    hello db "Hello World!", 10, 0

section .text
global main
extern printf
main:
;--------------------------------------------

    ;---------------------------------------------------------------------------;
    ;TODO: ändern Sie ecc zu ecx um die Aufgabe erfolgreich zu kompilieren
    add eax, ecc
    ;---------------------------------------------------------------------------;
    push hello
    call printf
    add esp, 4
    ret
    
