#include <stdlib.h>
#include <stdbool.h>

#include "fix_asm.h"
#include "helpers.h"
#include "math_fix.h"

#define DEBUG   1 ||

#define era(d,e,f,g) g
#define obscure(a,b,c,d) era(a,b,c,d)

static bool exhaustive = 0;
static bool fail = 0;

fix_t *gen_vec(float a, float b ,float c, fix_t *v)
{
    v[0] = fix_float2fix(a);
    v[1] = fix_float2fix(b);
    v[2] = fix_float2fix(c);
    return v;
}

void 
test_fix_add(fix_t a, fix_t b, fix_t expected)
{
    fix_t real = fix_add_asm(a, b);

    if(expected != real){
        handle_fail("test_fix_add", expected, real, a, b);
        
        if(!exhaustive)
            exit(1);

        fail |= 1;
    }
}

void 
test_fix_sub(fix_t a, fix_t b, fix_t expected)
{
    fix_t real = fix_sub_asm(a, b);

    if(expected != real){
        handle_fail("test_fix_sub", expected, real, a, b);
        
        if(!exhaustive)
            exit(1);

        fail |= 1;
    }
}

void 
test_fix_vec_add(fix_t *v1, fix_t *v2, fix_t *expected)
{
    fix_t real[3];
    fix_vec_add_asm(v1,v2,real);
    if(expected[0] != real[0] || expected[1] != real[1] || expected[2] != real[2]){
        handle_fail_vec("test_fix_vec_add", expected, real, v1, v2);

        if(!exhaustive)
            exit(1);
    
        fail |= 1;
    }
}

void 
test_fix_vec_sub(fix_t *v1, fix_t *v2, fix_t *expected)
{
    fix_t real[3];
    fix_vec_sub_asm(v1,v2,real);

    if(expected[0] != real[0] || expected[1] != real[1] || expected[2] != real[2]){
        handle_fail_vec("test_fix_vec_sub", expected, real, v1, v2); 
        if(!exhaustive)
            exit(1);
        fail |= 1;
    }
}
/*
long long int x = 4294967296 -1;
fix_t fix_mul_pos(fix_t a, fix_t b){
    fixu_t low = a * b;
    fixu_t high = (a >> 32) * (b >> 32);
    fixu_t middle1 = (a >> 32) * b; 
    fixu_t middle2 = a* (b >> 32);
    fixu_t middle = middle1 + middle2;
    fixu_t low2 = low + (middle << 32);
    high += (middle >> 32);
    printf("low: %llu, low2: %llu\n", low, low2);
    if(low2 > low){
        printf("Hi\n");
        high +=1;
    }
    if(middle < (middle1 + middle2)){
        printf("Hi2\n");
        high + (65536);
    }
    
    return  (fix_t)((low >> 26) | (high << 38)); 
}

fix_t fix_mul_c(fix_t a, fix_t b){
    fix_t expected;
    if((a < 0) && (b < 0)){
        expected = fix_mul_pos(-a,-b);
    }else if(a < 0){
        expected = -(fix_mul_pos(-a,b));
    }else if(b < 0){
        expected = -(fix_mul_pos(a,-b));
    }else{
        expected = fix_mul_pos(a,b);
   
    }
    return expected;
}
*/
void 
test_fix_mul(fix_t a, fix_t b, fix_t expected)
{
    fix_t real = fix_mul_asm(a, b);
//    printf("c: fix_t:%lld \n float:%f\n", fix_mul_c(a,b),fix_fix2float(fix_mul_c(a,b)));
    if(expected != real){
        handle_fail("test_fix_mul", expected, real, a, b);
        if(!exhaustive)
            exit(1);

        fail |= 1;
    }
}

void 
test_fix_vec_dot(fix_t *v1, fix_t *v2, fix_t expected)
{
    fix_t real = fix_vec_dot_asm(v1,v2);

    if(expected != real){
        handle_fail_dot("test_fix_vec_dot", expected, real, v1, v2);
        
        if(!exhaustive)
            exit(1);

        fail |= 1;
    }
}

void 
test_fix_vec_cross(fix_t *v1, fix_t *v2, fix_t *expected)
{
    fix_t real[3];
    fix_vec_cross_asm(v1,v2,real);


    if(expected[0] != real[0] || expected[1] != real[1] || expected[2] != real[2]){
        handle_fail_vec("test_fix_vec_cross", expected, real, v1, v2); 
        if(!exhaustive)
            exit(1);
        fail |= 1;
    }
}

int main(int argc, char **argv) 
{
    printHelp();

    if (argc == 2
        && atoi(argv[1]) == 1) {
        exhaustive = 1;
        exhaustiveOn();
    } else
        exhaustiveHelp();

    /**
     * ADD
     **/
    test_fix_add(fix_float2fix(0), fix_float2fix(0), 0);
    test_fix_add(fix_float2fix(-40), fix_float2fix(300), 17448304640);
    test_fix_add(fix_float2fix(1e-4), fix_float2fix(2),134224438);
    test_fix_add(fix_float2fix(14938123), fix_float2fix(99944212), 7709622727081984);
    test_fix_add(fix_float2fix(0.422), fix_float2fix(0.1), 35030826);
 
    if(!exhaustive)
        handle_pass("test_fix_add");

    /**
     * SUB
     **/
   test_fix_sub(fix_float2fix(0),fix_float2fix(0), 0);
    test_fix_sub(fix_float2fix(50),fix_float2fix(100), -3355443200);
    test_fix_sub(fix_float2fix(50),fix_float2fix(-50), 6710886400);
    test_fix_sub(fix_float2fix(1e-4),fix_float2fix(0.678), -45493098);
    test_fix_sub(fix_float2fix(14938123.12345),fix_float2fix(99944212.98765), -5704662334308352);

    if(!exhaustive)
        handle_pass("test_fix_sub");

    fix_t v1[3];
    fix_t v2[3];
    fix_t expected[3];
    
    /**
     * VEC_ADD
     **/
    test_fix_vec_add(gen_vec(0,0,0,v1),gen_vec(0,0,0,v2), gen_vec(0,0,0,expected));
    test_fix_vec_add(gen_vec(1,1,1,v1),gen_vec(-1,-1,-1,v2), gen_vec(0,0,0,expected));
    expected[0] = -436140171592;
    expected[1] = -3900597862400;
    expected[2] = 0;
    test_fix_vec_add(gen_vec(1.005,-123123.43532,0,v1),gen_vec(-6500.00001,65000,0,v2), expected);

    if(!exhaustive)
        handle_pass("test_fix_vec_add");

    /**
     * VEC_SUB
     **/
    test_fix_vec_sub(gen_vec(0,0,0,v1),gen_vec(0,0,0,v2), gen_vec(0,0,0,expected));
    test_fix_vec_sub(gen_vec(1.123,1.456,1.789,v1),gen_vec(1.123,1.456,1.789,v2), expected);
    expected[0] = -436140171592;
    expected[1] = -3900567453696;
    expected[2] = -6710880;
    test_fix_vec_sub(gen_vec(1.005,-123123.4375,0.0000001,v1),gen_vec(6500,-65000.453125,0.1,v2), expected);

    if(!exhaustive)
        handle_pass("test_fix_vec_sub");

    /**
     * fix_mul
     **/
    test_fix_mul(fix_float2fix(0),fix_float2fix(0),0);
    test_fix_mul(fix_float2fix(52),fix_float2fix(724),2526514511872);
    test_fix_mul(fix_float2fix(9231.918273),fix_float2fix(0.678),420050495049);
    test_fix_mul(fix_float2fix(-9231.918273),fix_float2fix(0.678),-420050495049);
    test_fix_mul(fix_float2fix(112.123),fix_float2fix(-4212.98765),-31700404337253);
    test_fix_mul(fix_float2fix(-8123.12),fix_float2fix(-212.987),116106319361700);
    
   
    if(!exhaustive)
        handle_pass("test_fix_mul");
    

    /**
     * VEC_DOT
     **/
    test_fix_vec_dot(gen_vec(1,1,1,v1), gen_vec(2,1,1,v2), 268435456);
    test_fix_vec_dot(gen_vec(-1,-2,-3,v1), gen_vec(2,1,1,v2), -469762048);
    test_fix_vec_dot(gen_vec(1e-3, 1e-2, 10, v1), gen_vec(2e-4,-10,33,v2), 22139214253);
    test_fix_vec_dot(gen_vec(-1,-2,-3,v1), gen_vec(2,1,1,v2), -469762048);
    test_fix_vec_dot(gen_vec(-10,-20,-33,v1), gen_vec(80,44,22,v2), -161463926784);  

    if(!exhaustive)
        handle_pass("test_fix_vec_dot");

    expected[0] = 0;
    expected[1] = 67108864;
    expected[2] = -67108864;

    test_fix_vec_cross(gen_vec(1,1,1,v1), gen_vec(2,1,1,v2), expected);

    expected[0] = 67108864;
    expected[1] = -335544320;
    expected[2] = 201326592;

    test_fix_vec_cross(gen_vec(-1,-2,-3,v1), gen_vec(2,1,1,v2), expected);

    expected[0] = 6733032304;
    expected[1] = -2080354;
    expected[2] = -671214;

    test_fix_vec_cross(gen_vec(1e-3, 1e-2, 10, v1), gen_vec(2e-4,-10,33,v2), expected);
 
    expected[0] = 67914170368;
    expected[1] = -162403450880;
    expected[2] = 77846282240;
 
    test_fix_vec_cross(gen_vec(-10,-20,-33,v1), gen_vec(80,44,22,v2), expected);  

    if(!exhaustive)
        handle_pass("test_fix_vec_cross");

    if(!fail)
        puts("All tests passed!\nPlease note: this is not a guarantee for a correct solution.\n");
}
