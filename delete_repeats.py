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

meta_path = r'/home/zach/Desktop/Datasets/Avatar_Frames_Clean'
# meta_path = r'/home/zach/Desktop/Snik/Avatar-main/test_images'
meta_dir = os.listdir(meta_path)
sorted_meta = sorted(meta_dir)

def get_folders():
	folder_names = []
	for folder_name in sorted_meta:
		if 693 > int(folder_name) or int(folder_name) > 1000:
			continue
		folder_names.append(folder_name)
	return folder_names

def goto_folder(name):
	im_path = os.path.join(meta_path, name)
	im_dir = os.listdir(im_path)
	sorted_folders = sorted(im_dir)
	return sorted_folders, im_path

def get_image(filename):
	# get one image
	image = Image.open(filename)
	image = image.resize((16, 16))
	data = np.asarray(image).astype(float)
	data = data - data.mean()
	data = data / (np.linalg.norm(data) + 1e-3)
	return data

def get_imgset(sorted_folders):
	#collect all images into ram.
	img_set = []
	name_set = []
	for filename in sorted_folders:
		im = get_image(filename)
		img_set.append(im)
		name_set.append(filename)
	return img_set, name_set

def subtracter(names, img_set):
	# if image is too similar (difference near 0), remove the almost repeated image
	names_to_remove = []
	# pick an image 
	for idx in range(len(img_set)):
		im = img_set[idx]
		if names[idx] in names_to_remove:
			continue
		for comparison_img_idx in range(len(img_set)):
			comparison_img = img_set[comparison_img_idx]
			comparison_filename = names[comparison_img_idx]
			if comparison_filename in names_to_remove:
				continue
			color_sums = 0
			for color in range(3):
				difference = np.subtract(im, comparison_img)
				difference = np.absolute(difference)
				sums = np.sum(difference[:,:,color])
				color_sums += sums
			if 0.0001 < sums < 0.3:
				# diff image ~ 10, same ~0.05
				names_to_remove.append(comparison_filename)
	return names_to_remove

def remover(names_to_remove):
	# delete filenames in names_to_remove
	print(f'removing {len(names_to_remove)} images.')
	[os.remove(removal_name) for removal_name in names_to_remove]

def main():
	# metafolder -> folders -> images -> find similar images -> remove them
	folder_names = get_folders()
	for name in folder_names:
		print(name)
		sorted_folders, im_path = goto_folder(name)
		os.chdir(im_path)
		img_set, name_set = get_imgset(sorted_folders)
		names_to_remove = subtracter(name_set, img_set)
		# print(names_to_remove)
		remover(names_to_remove)

if __name__ == "__main__":
	main()
