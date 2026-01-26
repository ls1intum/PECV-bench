/*
 * Copyright 2020, Lehrstuhl für Rechnerarchitektur & Parallele Systeme, Fakultät für Informatik, Technische Universität München
 */

#ifndef RC_VER03_FIXED_POINT_TRIANGLE_INTERSECTION_SRC_FIX_HPP_
#define RC_VER03_FIXED_POINT_TRIANGLE_INTERSECTION_SRC_FIX_HPP_

/*
 * Length of fixed point number in bytes
 */
#ifndef FIX_LEN
	#define FIX_LEN 8
#endif

#if FIX_LEN == 4
	typedef int fix_t;
	typedef unsigned int fixu_t;
#elif FIX_LEN == 8
	typedef int long long fix_t;
	typedef unsigned int long long fixu_t;
#else
	#error "FIX_LEN"
#endif

typedef int long long fix64_t;
typedef unsigned int long long fixu64_t;

/*
 * How many bits for fraction
 */
#ifndef FIX_FRAC
	#define FIX_FRAC 26
#endif

#ifdef __cplusplus
extern "C"
{
#endif

float fix_fix2float(fix_t f);
fix_t fix_float2fix(float f);
fix_t fix_mul(fix_t a, fix_t b);
fix_t fix_div(fix_t a, fix_t b);
void fix_vec_fix2float(const fix_t *i_vec, float *o_vec);
void fix_vec_float2fix(const float *i_vec, fix_t *o_vec);
void fix_vec_cross(const fix_t *v1, const fix_t *v2, fix_t *o);
fix_t fix_vec_dot(const fix_t *v1, const fix_t *v2);
void fix_vec_add(const fix_t *v1, const fix_t *v2, fix_t *o);
void fix_vec_sub(const fix_t *v1, const fix_t *v2, fix_t *o);
void fix_vec_mul(const fix_t *v1, const fix_t *v2, fix_t *o);

#ifdef __cplusplus
}
#endif

#endif
