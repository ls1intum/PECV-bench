/*
 * Copyright 2020, Lehrstuhl für Rechnerarchitektur & Parallele Systeme, Fakultät für Informatik, Technische Universität München
 */

#ifndef RC_VER04_FIXED_POINT_SPHERE_INTERSECTION_SRC_VEC_H_
#define RC_VER04_FIXED_POINT_SPHERE_INTERSECTION_SRC_VEC_H_


void float_vec_cross(const float *v1, const float *v2, float *o)
{
	o[0] = v1[1]*v2[2] - v1[2]*v2[1];
	o[1] = v1[2]*v2[0] - v1[0]*v2[2];
	o[2] = v1[0]*v2[1] - v1[1]*v2[0];
}


float float_vec_dot(const float *v1, const float *v2)
{
	return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2];
}



void float_vec_add(const float *v1, const float *v2, float *o)
{
	o[0] = v1[0] + v2[0];
	o[1] = v1[1] + v2[1];
	o[2] = v1[2] + v2[2];
}

void float_vec_sub(const float *v1, const float *v2, float *o)
{
	o[0] = v1[0] - v2[0];
	o[1] = v1[1] - v2[1];
	o[2] = v1[2] - v2[2];
}




#endif /* RC_VER04_FIXED_POINT_SPHERE_INTERSECTION_SRC_VEC_H_ */
