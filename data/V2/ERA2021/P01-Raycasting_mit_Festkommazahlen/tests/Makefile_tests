PROGRAM:=test
CCFLAGS=-O3 -m32
LDFLAGS=-m32

.PHONY: all

all:
	mkdir -p "tmp"
	nasm -g -f elf32 -dera=1 ../assignment/fix_vec_add.asm -o tmp/fix_vec_add.o
	nasm -g -f elf32 -dera=1 ../assignment/fix_vec_sub.asm -o tmp/fix_vec_sub.o
	nasm -g -f elf32 -dera=1 ../assignment/fix_mul.asm -o tmp/fix_mul.o
	nasm -g -f elf32 -dera=1 ../assignment/fix_vec_dot.asm -o tmp/fix_vec_dot.o
	nasm -g -f elf32 -dera=1 ../assignment/fix_vec_cross.asm -o tmp/fix_vec_cross.o
	nasm -g -f elf32 -dera=1 ../assignment/fix_add.asm -o tmp/fix_add.o
	nasm -g -f elf32 -dera=1 ../assignment/fix_sub.asm -o tmp/fix_sub.o
	gcc -g -m32 -o test src/test.c tmp/fix_vec_sub.o tmp/fix_vec_add.o tmp/fix_mul.o tmp/fix_vec_dot.o tmp/fix_vec_cross.o tmp/fix_add.o tmp/fix_sub.o
	
clean:
	rm -f test
	rm -rf tmp

