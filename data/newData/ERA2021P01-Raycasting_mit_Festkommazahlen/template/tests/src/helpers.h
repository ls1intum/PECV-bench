#include <stdio.h>

const char *const msg =
"    __________  ___       _________________________________\n"
"   / ____/ __ \\/   |     /_  __/ ____/ ___/_  __/ ____/ __ \\\n"
"  / __/ / /_/ / /| |______/ / / __/  \\__ \\ / / / __/ / /_/ /\n"
" / /___/ _, _/ ___ /_____/ / / /___ ___/ // / / /___/ _, _/\n" 
"/_____/_/ |_/_/  |_|    /_/ /_____//____//_/ /_____/_/ |_|\n";

const char *const dash = "------------------------------------------------------------";

void
printHelp()
{
    puts(dash);
    puts(dash);
    puts(msg);
    puts(dash);
}

void
exhaustiveHelp()
{
    puts(dash);
    puts("----     Start with $ ./test 1 for exhaustive mode      ----");
    puts(dash);
}

void
exhaustiveOn()
{
    puts(dash);
    puts("----            Testing in exhaustive mode              ----");
    puts(dash);
}

void
handle_fail(const char *msg, fix_t expected, fix_t real, fix_t a, fix_t b)
{
    printf("Error: test %s failed!\n", msg);
    printf("[INPUTS] {%lld, %lld} [FIX], {%f, %f} [FLOAT]\n", a, b, fix_fix2float(a), fix_fix2float(b));
    printf("[FIX] Expected [%lld], got [%lld]\n", expected, real);
    printf("[FLOAT] Expected [%f], got [%f]\n", fix_fix2float(expected), fix_fix2float(real));
    puts(dash);
}

void
vec_inp_format(fix_t *v1, fix_t *v2)
{
    printf("[INPUTS] v1: {%lld, %lld, %lld}, v2: {%lld, %lld, %lld} [FIX]\n", v1[0], v1[1], v1[2], v2[0], v2[1], v2[2]);
    printf("[INPUTS] v1: {%f, %f, %f}, v2: {%f, %f, %f} [FLOAT]\n", 
    fix_fix2float(v1[0]), fix_fix2float(v1[1]), fix_fix2float(v1[2]), fix_fix2float(v2[0]), fix_fix2float(v2[1]), fix_fix2float(v2[2]));
}

void
handle_fail_vec(const char *msg, fix_t *expected, fix_t *real, fix_t *v1, fix_t *v2)
{
    printf("Error: test %s failed!\n", msg);
    vec_inp_format(v1, v2);
    printf("[FIX] Expected (%lld,%lld,%lld), got (%lld,%lld,%lld)\n", expected[0],expected[1],expected[2], real[0], real[1], real[2]);
    printf("[FLOAT] Expected (%f,%f,%f), got (%f,%f,%f)\n", fix_fix2float(expected[0]), fix_fix2float(expected[1]), fix_fix2float(expected[2]),fix_fix2float(real[0]), fix_fix2float(real[1]), fix_fix2float(real[2]));
    puts(dash);
}

void
handle_fail_dot(const char *msg, fix_t expected, fix_t real, fix_t *v1, fix_t *v2)
{
    printf("Error: test %s failed!\n", msg);
    vec_inp_format(v1, v2);
    printf("[FIX] Expected [%lld], got [%lld]\n", expected, real);
    printf("[FLOAT] Expected [%f], got [%f]\n", fix_fix2float(expected), fix_fix2float(real));
    puts(dash);
}


void
handle_pass(const char *msg)
{
    printf("Success: test %s passed!\n", msg);
    puts(dash);
}