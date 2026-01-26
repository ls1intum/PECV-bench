/*
 * Copyright 2010 Martin Schreiber
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */



#ifndef BITMAP24_HPP
#define BITMAP24_HPP

#include <string>


/**
 * \brief	store image data to a bitmap file
 *
 * store the 24 bit rgb image data in the array data[] to a 24 bit bitmap file
 */
class Bitmap24
{
public:
	int width;			///< bitmap width
	int height;			///< bitmap height
	char *data;			///< allocated bitmap data where the 24 bit bitmap data has to be loaded before the bitmap can be stored

	Bitmap24();
	Bitmap24(int i_width, int i_height);

	~Bitmap24();

	void resize_buffer(
			int i_width,
			int i_height
		);

	void save(
			const std::string &i_filename
		);

	void set(
			int i_y,
			int i_x,
			char i_r,
			char i_g,
			char i_b
	);
};

#endif
