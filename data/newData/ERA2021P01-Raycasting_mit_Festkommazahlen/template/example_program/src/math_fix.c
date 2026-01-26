/*
 * Copyright 2020, Lehrstuhl für Rechnerarchitektur & Parallele Systeme, Fakultät für Informatik, Technische Universität München
 */

#ifndef RC_VER04_FIXED_POINT_TRIANGLE_INTERSECTION_SRC_FIX_HPP_
#define RC_VER04_FIXED_POINT_TRIANGLE_INTERSECTION_SRC_FIX_HPP_

#include "math_fix.h"
#include "math.h"

#define FIX_LEN 8

typedef int long long fix_t;
typedef unsigned int long long fixu_t;

typedef int long long fix64_t;
typedef unsigned int long long fixu64_t;

extern fix_t fix_vec_add_asm(const fix_t* v0,const fix_t* v1, fix_t* o);
extern fix_t fix_vec_sub_asm(const fix_t* v0,const fix_t* v1, fix_t* o);
    

/*
 * How many bits for fraction
 */
#define FIX_FRAC 26

inline float fix_fix2float(fix_t f)
{
    return ((double) f / (double)((fix_t)1 << FIX_FRAC));
}

inline fix_t fix_float2fix(float f)
{
    return (fix_t)((double)f * ((fix_t)1 << FIX_FRAC));
}

extern fix_t fix_mul_asm(fix_t a, fix_t b);

inline fix_t fix_mul(fix_t a, fix_t b)
{
	return fix_mul_asm(a,b);
}


inline fix_t fix_div(fix_t a, fix_t b)
{
	// Care about DIV/0 since the program would setfault :-(
	if (b == 0)
		return (fix_t)((~(fixu_t)0) >> 1);

	return (a << FIX_FRAC)/b;
}


inline void fix_vec_fix2float(const fix_t *i_vec, float *o_vec)
{
	o_vec[0] = fix_fix2float(i_vec[0]);
	o_vec[1] = fix_fix2float(i_vec[1]);
	o_vec[2] = fix_fix2float(i_vec[2]);
}


inline void fix_vec_float2fix(const float *i_vec, fix_t *o_vec)
{
	o_vec[0] = fix_float2fix(i_vec[0]);
	o_vec[1] = fix_float2fix(i_vec[1]);
	o_vec[2] = fix_float2fix(i_vec[2]);
}



extern void fix_vec_cross_asm(const fix_t *v1, const fix_t *v2, fix_t *o);

inline void fix_vec_cross(const fix_t *v1, const fix_t *v2, fix_t *o)
{
    fix_vec_cross_asm(v1,v2,o);
    return;
}


extern fix_t fix_vec_dot_asm(const fix_t *v1, const fix_t *v2);

inline fix_t fix_vec_dot(const fix_t *v1, const fix_t *v2)
{
	return fix_vec_dot_asm(v1,v2);
}


inline void fix_vec_add(const fix_t *v1, const fix_t *v2, fix_t *o)
{
    fix_vec_add_asm(v1,v2,o);
    return;
}

inline void fix_vec_sub(const fix_t *v1, const fix_t *v2, fix_t *o)
{
    fix_vec_sub_asm(v1,v2,o);
    return;
}

inline void fix_vec_mul(const fix_t *v1, const fix_t *v2, fix_t *o)
{
	o[0] = fix_mul(v1[0], v2[0]);
	o[1] = fix_mul(v1[1], v2[1]);
	o[2] = fix_mul(v1[2], v2[2]);
}


#endif
