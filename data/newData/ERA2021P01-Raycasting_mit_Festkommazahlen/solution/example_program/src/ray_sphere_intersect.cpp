/*
 * Copyright 2020, Lehrstuhl für Rechnerarchitektur & Parallele Systeme, Fakultät für Informatik, Technische Universität München
 */


#include "ray_sphere_intersect.h"
#include "math_float.h"
#include <cmath>

bool ray_sphere_intersect(
		const float *origin,
		const float *dir,
		const float *center,
		const float radius
)
{
	const float *o = origin;
	const float *u = dir;
	const float *c = center;

	const float r2 = radius;

	// https://en.wikipedia.org/wiki/Line%E2%80%93sphere_intersection
	float oc[3];
	float_vec_sub(o, c, oc);

	float a = float_vec_dot(u, oc);
	float b = float_vec_dot(oc, oc) - r2;
	float lap = a*a - b;

	if (lap < 0)
		return false;

	return true;
}


