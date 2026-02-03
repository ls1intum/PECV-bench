/*
 * Copyright 2020, Lehrstuhl für Rechnerarchitektur & Parallele Systeme, Fakultät für Informatik, Technische Universität München
 */

#ifndef RAY_TRIANGLE_INTERSECT_H_
#define RAY_TRIANGLE_INTERSECT_H_

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

bool ray_triangle_intersect(
		const float *orig,
		const float *dir,
		const float *v0,
		const float *v1,
		const float *v2,
		float *o_uvt
);

bool ray_triangle_intersect_fix(
		const fix_t *orig,
		const fix_t *dir,
		const fix_t *v0,
		const fix_t *v1,
		const fix_t *v2,
		fix_t *o_uvt
);



#endif /* RAY_TRIANGLE_INTERSECT_H_ */
