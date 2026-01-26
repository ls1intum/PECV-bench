/*
 * Copyright 2020, Lehrstuhl für Rechnerarchitektur & Parallele Systeme, Fakultät für Informatik, Technische Universität München
 */

#include <iostream>
#include <fstream>
#include <cstring>

#include <cmath>
#include "Bitmap24.hpp"
#include "math_float.h"
#include "math_fix.h"
#include "ray_triangle_intersect.h"
#include "ray_sphere_intersect.h" 
#include "common.hpp"
#include "progressbar.hpp"

#define fix_whole(len, frac) \
	((len * 8) - frac)


const char *scene_bin = "scene.bin";

int main(int argc, char **argv)
{
	int width = 320;
	int height = 240;
	//int height = 40;

	int s = 2;
	width *= s;
	height *= s;

	progressbar bar(height);

	Bitmap24 bitmap;
	bitmap.resize_buffer(width, height);

	/*
	 * Generate black background
	 */
	for (int i = 0; i < height; i++)
		for (int j = 0; j < width; j++)
			bitmap.set(i, j, 0, 0, 0);

	float *depth_buffer = new float[width*height];

	for (int i = 0; i < height; i++)
		for (int j = 0; j < width; j++)
			depth_buffer[i*width+j] = 1e10;

	std::ifstream preamble;
	preamble.open(scene_bin, std::ios::binary | std::ios::in);
	
	uint64_t it_count;
	uint16_t fix_frac;
	uint8_t fix_len;
	uint8_t use_float;

	char magic[MAGIC_LEN];
	preamble.read(magic, MAGIC_LEN);

	//Check for magic string
	if(std::memcmp(magic, MAGIC, MAGIC_LEN)) {
		std::cout << "Invalid file format.\n";
		exit(EXIT_FAILURE);
	}

	//Read in preamble data
	preamble.read((char *)&it_count, ITCOUNT_SIZE);
	preamble.read((char *)&fix_frac, FIX_FRAC_SIZE);
	preamble.read((char *)&fix_len, FIX_LEN_SIZE);
	preamble.read((char *)&use_float, USE_FIX_SIZE);	
	preamble.close();

	if((fix_len != FIX_LEN) && !use_float) {
		std::cout << "Length mismatch for fix point numbers. Expected " << fix_len << ", got " << FIX_LEN << "\nRebuild binary file accordingly.\n";
		exit(EXIT_FAILURE);
	}

	if((fix_frac != FIX_FRAC) && !use_float) {
		std::cout << "Length mismatch for fractional part. Expected " << fix_frac << ", got " << FIX_FRAC << "\nRebuild binary file accordingly.\n";
		exit(EXIT_FAILURE);
	}

	if(!use_float)
		std::cout << "Using " << fix_whole(fix_len, fix_frac) << "." << fix_frac << " fixpoint numbers.\n";
	else
		std::cout << "Using floats.\n";

	double aspect_scale = 1.0/std::max(width-1, height-1);


	//Read in file
	std::ifstream fin;
	fin.open(scene_bin, std::ios::binary | std::ios::in);
	fin.seekg(DATA_OFFSET);

	ssize_t num_bytes;
	if(use_float || fix_len == 4)
		num_bytes = it_count * (3 * 4 * sizeof(float));
	else
		num_bytes = it_count * (3 * 4 * sizeof(fix_t));

	uint8_t *data = (uint8_t *)std::malloc(num_bytes);
	fin.read((char *)data, num_bytes);
	fin.close();

	fix_t origin[3] = {0, 0, fix_float2fix(1.5)};

	#pragma omp parallel for
	for (int i = 0; i < height; i++)
	{
		float ry = i*aspect_scale;
		float y = ry - 0.5;

		#pragma omp critical
			bar.update();

		for (int j = 0; j < width; j++)
		{
			float rx = j*aspect_scale;
			float x = rx - 0.5;

			fix_t dir[3] = {fix_float2fix(x), fix_float2fix(y), fix_float2fix(-1)};
			float dir_f[3] = {x, y, (-1)};

			/*
			* Normalize directory for sphere intersection test
			*/
			float n2 = float_vec_dot(dir_f, dir_f);
			float norm = 1.0/std::sqrt(n2);

			int to_copy = sizeof(float) * 3;

			float dirn[3];
			dirn[0] = dir[0] * norm;
			dirn[1] = dir[1] * norm;
			dirn[2] = dir[2] * norm;

			uint8_t *ptr = data;
			for(uint64_t k = 0; k < num_bytes;){
				fix_t v0[3];
				fix_t v1[3];
				fix_t v2[3];
				fix_t color[3];
				fix_t uvt[3];

				int to_read = sizeof(fix_t) * 3;

				//This is ugly..
				memcpy((void *)v0, (void *)ptr, to_read);
				ptr += to_read;
				memcpy((void *)v1, (void *)ptr, to_read);
				ptr += to_read;
				memcpy((void *)v2, (void *)ptr, to_read);
				ptr += to_read;
				memcpy((void *)color, (void *)ptr, to_read);
				ptr += to_read;

				k += 4 * to_read;

				/*
				 * Compute center of bounding sphere
				 */
				float center[3];
				center[0] = (v0[0] + v1[0] + v2[0])*(1.0/3.0);
				center[1] = (v0[1] + v1[1] + v2[1])*(1.0/3.0);
				center[2] = (v0[2] + v1[2] + v2[2])*(1.0/3.0);

				float v0_f[3];
				float v1_f[3];
				float v2_f[3];
				float origin_f[3];

				fix_vec_fix2float(v0, v0_f);
				fix_vec_fix2float(v1, v1_f);
				fix_vec_fix2float(v2, v2_f);
				fix_vec_fix2float(origin, origin_f);

				/*
				 * Compute squared radius of bounding sphere
				 */
				float radius2 = 0;
				float cv0[3];
				float cv1[3];
				float cv2[3];
				float_vec_sub(center,v0_f,cv0);
				float_vec_sub(center,v1_f,cv1);
				float_vec_sub(center,v2_f,cv2);
				radius2 = std::max(radius2, float_vec_dot(cv0,cv0));
				radius2 = std::max(radius2, float_vec_dot(cv1,cv1));
				radius2 = std::max(radius2, float_vec_dot(cv2,cv2));

				if (!ray_sphere_intersect(origin_f, dirn, center, radius2))
					continue;

				bool retval = ray_triangle_intersect_fix(
						origin, dir,
						v0, v1, v2,
						uvt
				);

				if (!retval)
					continue;

				float uvt_f[3];
				fix_vec_fix2float(uvt, uvt_f);

				float color_f[3];
				fix_vec_fix2float(color, color_f);

				if (depth_buffer[i*width + j] > uvt_f[2])
				{
					bitmap.set(i, j, color_f[2], color_f[1], color_f[0]);

					depth_buffer[i*width + j] = uvt_f[2];
				}
			}
		}
	}

	std::cout << std::endl;

	std::string outfile = "era_ausgabe.bmp";

	std::cout << "Writing output to " << outfile << std::endl;
	bitmap.save(outfile);

	delete [] depth_buffer;
	std::free(data);
	return 0;
}
