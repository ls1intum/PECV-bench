AS=nasm
CFLAGS=-g -f elf32

NAME=helloWorld

all:
	$(AS) $(CFLAGS) $(NAME).asm -o $(NAME).o
	gcc -m32 $(NAME).o -g -o $(NAME).out -fno-pie -no-pie 

clean:
	rm $(NAME).o
	rm $(NAME).out
