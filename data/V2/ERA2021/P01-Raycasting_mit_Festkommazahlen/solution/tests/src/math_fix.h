#ifndef MATH_FIX_H
#define MATH_FIX_H

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

float fix_fix2float(fix_t f)
{
    return ((double) f / (double)((fix_t)1 << FIX_FRAC));
}

fix_t fix_float2fix(float f)
{
    return (fix_t)((double)f * ((fix_t)1 << FIX_FRAC));
}

void fix_vec_fix2float(const fix_t *i_vec, float *o_vec)
{
	o_vec[0] = fix_fix2float(i_vec[0]);
	o_vec[1] = fix_fix2float(i_vec[1]);
	o_vec[2] = fix_fix2float(i_vec[2]);
}


void fix_vec_float2fix(const float *i_vec, fix_t *o_vec)
{
	o_vec[0] = fix_float2fix(i_vec[0]);
	o_vec[1] = fix_float2fix(i_vec[1]);
	o_vec[2] = fix_float2fix(i_vec[2]);
}


#endif
