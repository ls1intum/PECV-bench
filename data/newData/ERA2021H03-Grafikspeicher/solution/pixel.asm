;%include "io.inc"; <-- Uncomment for usage in SASM

;-------Do not modify this section-------
section .bss
    display_start RESB 8294400
    buf resb 16
section .data 
    message db "Wert in Speicherzelle (0x%08X, 0x%08X) = 0x%08X", 10, 10, 0
    value db "Wert: 0x%08X", 10, 0
    get_x db "Bitte Wert für x eingeben", 10, 0
    get_y db "Bitte Wert für y eingeben", 10, 0
    get_color db "Bitte RBG-Wert für neue Farbe eingeben", 10, 0
section .text
global main
extern printf
extern atoi
extern fgets
main:
 mov ebp, esp
;set pixel with parameters from stdin
 ;save registers
 push ebx
 push edi
 push esi
 
 ;print instruction
 push get_x
 call printf
 add esp, 4
 
 ;syscall to read x from stdin
 mov eax, 3      ; sys_read
 mov ebx, 0      ; stdin
 mov ecx, buf    ; buffer 
 mov edx, 5      ; size in byte
 int 80h
 
 ;convert x from ASCII to int 
 push buf
 call atoi
 add esp, 4
 push eax
 
 ;print instruction
 push get_y
 call printf
 add esp, 4
 
 ;clear buffer
 mov dword [buf], 0
 mov dword [buf + 4], 0
 
 ;syscall to read y from stdin
 mov eax, 3      ; sys_read
 mov ebx, 0      ; stdin
 mov ecx, buf    ; buffer (memory address, where read should save 4 byte)
 mov edx, 5      ; read byte count
 int 80h

 ;convert y from ASCII to int
 push buf
 call atoi
 add esp, 4

 ;mov values to right registers
 mov ebx, eax
 pop eax
 
 ;save values for later
 push eax
 push ebx


 ;TODO: calculate position; result in esi
 
 mov esi, display_start
 mov edi, 4
 mul edi
 add esi, eax
 mov eax, 7680
 mul ebx
 add esi, eax
 mov ecx, [esi]

 ;get coordinates
 pop ebx
 pop eax 
 
 ;save coordinates and position for later
 push eax
 push ebx
 push esi
 
 ; print initial value at position
 push ecx
 push ebx
 push eax
 push message
 call printf
 add esp, 16 

 
 ; print instruction
 push get_color
 call printf
 add esp, 4
 
 ; clear buffer
 mov dword [buf], 0
 mov dword [buf + 4], 0
 
 ;read color from stdin
 mov eax, 3      ; sys_read
 mov ebx, 0      ; stdin
 mov ecx, buf    ; buffer (memory address, where read should save 4 byte)
 mov edx, 9      ; read byte count
 int 80h
 
 ;convert color from ASCII to int   
 push buf
 call atoi
 add esp, 4
 mov ecx, eax
  
 ;get coordinates
 mov eax, [esp +8]
 mov ebx, [esp + 4] 
 
 call set_pixel
 
 ;get position and coordinates
 pop edx
 pop ebx
 pop eax

 ;get new value at position
 mov ecx, [edx]

 ;print new value
 push ecx
 push ebx
 push eax
 push message
 call printf
 add esp, 16
 
 ;restore values
 pop esi
 pop edi
 pop ebx
 ret

    set_pixel:
        push ebx
        push esi
        push edx
        mov edx, 4
        mul edx ; eax = x*4
        mov esi, eax ; eax zwischenspeichern
        mov eax,7680 
        mul ebx ; eax = 7680 * y
        add eax, esi ; eax += x * 4
        add eax, display_start ; basis Adresse addieren
        mov [eax], ecx ; rbg in berechnete Adresse schreiben
        pop edx
        pop esi
        pop ebx
        ret
