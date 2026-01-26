#include "math_fix.h"

extern fix_t fix_add_asm(fix_t, fix_t);
extern fix_t fix_sub_asm(fix_t, fix_t);
extern void fix_vec_add_asm(fix_t *, fix_t *, fix_t *);
extern void fix_vec_sub_asm(fix_t *, fix_t *, fix_t *);
extern fix_t fix_mul_asm(fix_t, fix_t);
extern fix_t fix_vec_dot_asm(fix_t *, fix_t *);
extern void fix_vec_cross_asm(fix_t *, fix_t *,fix_t *);
