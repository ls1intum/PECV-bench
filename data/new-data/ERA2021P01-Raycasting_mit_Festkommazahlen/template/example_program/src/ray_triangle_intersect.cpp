/*
 * Copyright 2020, Lehrstuhl für Rechnerarchitektur & Parallele Systeme, Fakultät für Informatik, Technische Universität München
 */


#include "ray_triangle_intersect.h"
#include <stdio.h>
#define RAY_TRIANGLE_INTERSECT_FIX_DOT		1
#define RAY_TRIANGLE_INTERSECT_FIX_CROSS	1
#define RAY_TRIANGLE_INTERSECT_FIX_ALL		1

#define UV_EPSILON		(double)1e-2
#define NUM_EPSILON		(1e-7)



#include "math_fix.h"

void fix_vec_cross_(const fix_t v1[3], const fix_t v2[3], fix_t o[3])
{
	fix_vec_cross(v1, v2, o);
}

fix_t fix_vec_dot_(const fix_t v1[3], const fix_t v2[3])
{
	return fix_vec_dot(v1, v2);
}


#include "math_fix.h"

bool ray_triangle_intersect_fix(
		const fix_t orig[3],
		const fix_t dir[3],
		const fix_t v0[3],
		const fix_t v1[3],
		const fix_t v2[3],
		fix_t *o_uvt
)
{
	fix_t v0v1[3];
	fix_vec_sub(v1, v0, v0v1);

	fix_t v0v2[3];
	fix_vec_sub(v2, v0, v0v2);

	fix_t pvec[3];
	fix_vec_cross_(dir, v0v2, pvec);

	fix_t det = fix_vec_dot_(v0v1, pvec);

	fix_t eps = fix_float2fix(NUM_EPSILON);

	if (det < eps)
		return false;

	fix_t tvec[3];
	fix_vec_sub(orig, v0, tvec);

	fix_t invDet = fix_div(fix_float2fix(1), det);


	fix_t u = fix_mul(fix_vec_dot_(tvec, pvec), invDet);

	if (u < -UV_EPSILON || u > fix_float2fix(1+UV_EPSILON))
		return false;

	fix_t qvec[3];
	fix_vec_cross_(tvec, v0v1, qvec);

	fix_t v = fix_mul(fix_vec_dot_(dir, qvec), invDet);
	if (v < -UV_EPSILON || u + v > fix_float2fix(1+UV_EPSILON))
		return false;

	fix_t t = fix_mul(fix_vec_dot_(v0v2, qvec), invDet);

	o_uvt[0] = u;
	o_uvt[1] = v;
	o_uvt[2] = t;

	return true;
}



/*
 * Everything with fixed point
 */
bool ray_triangle_intersect(
		const float *orig,
		const float *dir,
		const float *v0,
		const float *v1,
		const float *v2,
		float *o_uvt
)
{
	fix_t fix_orig[3];
	fix_t fix_dir[3];
	fix_t fix_v0[3];
	fix_t fix_v1[3];
	fix_t fix_v2[3];
	fix_t fix_o_uvt[3];

	fix_vec_float2fix(orig, fix_orig);
	fix_vec_float2fix(dir, fix_dir);
	fix_vec_float2fix(v0, fix_v0);
	fix_vec_float2fix(v1, fix_v1);
	fix_vec_float2fix(v2, fix_v2);

	bool retval = ray_triangle_intersect_fix(
			fix_orig, fix_dir,
			fix_v0, fix_v1, fix_v2,
			fix_o_uvt
		);

	fix_vec_fix2float(fix_o_uvt, o_uvt);
	return retval;
}


