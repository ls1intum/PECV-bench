/*
 * Copyright 2020, Lehrstuhl für Rechnerarchitektur & Parallele Systeme, Fakultät für Informatik, Technische Universität München
 */

#ifndef RC_VER04_FIXED_POINT_SPHERE_INTERSECTION_SRC_VEC_H_
#define RC_VER04_FIXED_POINT_SPHERE_INTERSECTION_SRC_VEC_H_


#ifdef __cplusplus
extern "C"
{
#endif

void float_vec_cross(const float *v1, const float *v2, float *o);
float float_vec_dot(const float *v1, const float *v2);
void float_vec_add(const float *v1, const float *v2, float *o);
void float_vec_sub(const float *v1, const float *v2, float *o);

#ifdef __cplusplus
}
#endif

#endif /* RC_VER04_FIXED_POINT_SPHERE_INTERSECTION_SRC_VEC_H_ */
