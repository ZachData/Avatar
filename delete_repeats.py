'''
Given a folder of ~1000 images,
	delete all repeated images. 
I think that python will be unhappy if I delete things 
	while inside of a for-loop over those very things.
	I want to create a system that keeps tabs on the repeats, 
		then deletes them after the for-loop is over.
'''

import os
from PIL import Image, ImageOps
import numpy as np 

meta_path = r'C:\Users\M\Desktop\delete-repeats\data'
# im_path = r'/home/zach/Desktop/Snik/Avatar-main/00000'
meta_dir = os.listdir(meta_path)
# sorted_dir = sorted(im_dir)
# dir_len = len(im_dir)
# os.chdir(im_path)


def get_image(filename):
	# get one image
	image = Image.open(filename)
	# image = ImageOps.grayscale(image)
	image = image.resize((16, 16))
	data = np.asarray(image).astype(float)
	data = data - data.mean()
	data = data / (np.linalg.norm(data) + 1e-3)
	# print(data.mean(), np.linalg.norm(data))

	return data

def mark_repeats(im1, im2, tabs, filename):
	# compare two images
	print(np.array_equal(im1, im2))
		# print(im1[:,:,0].shape, im2[:,:,0].shape)
		# print('found True')
		# tabs.append(filename)

def main():
	# collect filenames to delete in tabs
	# track to only go forwards, removing repeats
	for folder_name in meta_dir:
		print(folder_name)
		im_path = os.path.join(meta_path, folder_name)
		im_dir = os.listdir(im_path)
		sorted_dir = sorted(im_dir)
		dir_len = len(im_dir)
		os.chdir(im_path)
		tabs = []
		im_tracker = 0
		for filename in sorted_dir:
			im_tracker += 1
			im = get_image(filename)
			for comparison_filename in sorted_dir[im_tracker:dir_len]:
				if comparison_filename in tabs:
					continue
				comparison_img = get_image(comparison_filename)
				color_sums = 0
				for color in range(3):
					difference = np.subtract(im, comparison_img)
					difference = np.absolute(difference)
					sums = np.sum(difference[:,:,color])
					color_sums += sums
				if 0.0001 < sums < 0.3:
					# diff image ~ 10, same ~0.05
					tabs.append(comparison_filename)
				# print(filename)

		# delete filenames in tabs
		print(len(tabs))
		for repeat in tabs:
			os.remove(repeat)

main()


# for i in sorted_dir:
# 	print(i)