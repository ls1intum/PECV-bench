OBJS:=src/main.o src/Bitmap24.o src/ray_sphere_intersect.o src/ray_triangle_intersect.o

MATHOBJ:=src/math_float.o src/math_fix.o
NASMOBJ:=tmp/fix_vec_add.o tmp/fix_vec_sub.o tmp/fix_mul.o tmp/fix_vec_dot.o tmp/fix_vec_cross.o tmp/fix_add.o tmp/fix_sub.o

PROGRAM:=rc
CXXFLAGS=-O3 -fopenmp -m32
CCFLAGS=-O3 -fopenmp -m32
LDFLAGS=-fopenmp -m32

all:	$(PROGRAM)

rc:	$(OBJS)
	mkdir -p "tmp"
	nasm -g -f elf32 -Dera=1 ../assignment/fix_vec_add.asm -o tmp/fix_vec_add.o
	nasm -g -f elf32 -Dera=1 ../assignment/fix_vec_sub.asm -o tmp/fix_vec_sub.o
	nasm -g -f elf32 -Dera=1 ../assignment/fix_mul.asm -o tmp/fix_mul.o
	nasm -g -f elf32 -Dera=1 ../assignment/fix_vec_dot.asm -o tmp/fix_vec_dot.o
	nasm -g -f elf32 -Dera=1 ../assignment/fix_vec_cross.asm -o tmp/fix_vec_cross.o
	nasm -g -f elf32 -Dera=1 ../assignment/fix_add.asm -o tmp/fix_add.o
	nasm -g -f elf32 -Dera=1 ../assignment/fix_sub.asm -o tmp/fix_sub.o
	gcc -c -m32 src/math_float.c -o src/math_float.o
	gcc -c -m32 src/math_fix.c -o src/math_fix.o
	g++ $(OBJS) $(MATHOBJ) $(NASMOBJ) -o $(PROGRAM) $(LDFLAGS)

clean:
	rm -f $(OBJS) $(PROGRAM)
	rm -f era_ausgabe.bmp
	rm -f $(NASMOBJ)
	rm -f $(MATHOBJ)
	rm -rf "tmp"

$(OBJS): $(wildcard src/*.hpp) $(wildcard src/*.h)
