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

im_path = r'C:\Users\M\Desktop\delete-repeats\00000'
im_dir = os.listdir(im_path)
dir_len = len(im_dir)
os.chdir(im_path)


def get_image(filename):
	# get one image
	image = Image.open(filename)
	image = ImageOps.grayscale(image)
	data = np.asarray(image)
	return data

def mark_repeats(im1, im2, tabs, filename):
	# compare two images
	print(np.array_equal(im1, im2))
		# print(im1[:,:,0].shape, im2[:,:,0].shape)
		# print('found True')
		# tabs.append(filename)

def main():
	# collect filenames to delete in tabs
	# im_tracker to not look over things we have already seen
	# tabs to not delete things we are using in a for-loop
	# tabs = []
	im_tracker = 0
	for filename in im_dir:
		# im_tracker += 1
		im = get_image(filename)
		# print(im_dir[im_tracker:dir_len])
		ims = 0
		for comparison_filename in im_dir[im_tracker:dir_len]:
			# if comparison_filename in tabs:
			# 	continue
			comparison_img = get_image(comparison_filename)
			# mark_repeats(im, comparison_img, tabs, comparison_filename)
			difference = np.subtract(im, comparison_img)
			sums = np.sum(difference)
			print((sums), ims)
			ims += 1
	# delete filenames in tabs
	print(tabs)
	# for repeat in tabs:
	# 	os.remove(repeat)

# main()

im0 = np.asarray(Image.open(r'img00000000.png'))
im1 = np.asarray(Image.open(r'img00000010.png'))
im2 = np.asarray(Image.open(r'img00000011.png'))
print(np.sum(im1[:,:,0]-im2[:,:,0]))
print(np.sum(im2[:,:,0]-im1[:,:,0]))

