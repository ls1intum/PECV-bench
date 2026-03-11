/*
 * Copyright 2020, Lehrstuhl für Rechnerarchitektur & Parallele Systeme, Fakultät für Informatik, Technische Universität München
 */

#define MAGIC "ERA2"
#define MAGIC_LEN	4

#define ITCOUNT_SIZE sizeof(uint64_t)
#define FIX_FRAC_SIZE sizeof(uint16_t)
#define FIX_LEN_SIZE sizeof(uint8_t)
#define USE_FIX_SIZE sizeof(uint8_t)

//Whether or not we write as floats, we still save this information and offset accordingly later
#define DATA_OFFSET (MAGIC_LEN + ITCOUNT_SIZE + FIX_FRAC_SIZE + FIX_LEN_SIZE + USE_FIX_SIZE)
