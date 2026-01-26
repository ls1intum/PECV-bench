;%include "io.inc"; <-- Uncomment for usage in SASM

;Usage: 1. Run Program
;       2. Insert value for x in decimal (max 4 digits)
;       3. Insert value for y in decimal (max 4 digits)
;       4. Insert RGB color (0xRRGGBB) in decimal (e.g. 16711680 for red, 16777215 for white and 0 for black)
;       5. Check if the value was changed accordingly

;Input values with more than 4 digits will partially stay in stdin and be read later which leads to wrong output

;Usage in SASM: Input from stdin has to be put in the input field in SASM before execution
;Additionally in SASM all input values have to have the right size which means 4 digits for x and y, 8 digits for the RGB color (preceding zeros, e.g. 0001) 


;---TODO: INSERT FORMULA HERE: X
;---Add Code at the 3rd TODO which calculates the position


;-------Do not modify this section-------
section .bss
    display_start RESD 8294400
    buf resd 2
section .data 
    message db 10, "Wert in Speicherzelle (0x%08X, 0x%08X) = 0x%08X", 10, 10, 0
    value db "Wert: 0x%08X", 10, 0
    get_x db "Bitte Wert für x eingeben", 10, 0
    get_y db "Bitte Wert für y eingeben", 10, 0
    get_color db "Bitte RBG-Wert für neue Farbe eingeben", 10, 0
section .text
global main
extern printf
extern atoi
extern fgets
;---------------------------------------

;---TODO implement set_pixel here---
set_pixel: 
        ret
        
        
;------------------------------

;-------Do not modify anything below except the one TODO-------
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


 ;TODO: calculate position; (EAX:x, EBX:y, display_start is the base address needed) result (address) in ESI
 ;Attention: save all registers you modify except eax,ebx and esi

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
