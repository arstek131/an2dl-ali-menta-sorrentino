#!/usr/bin/python

import os, random, shutil

print("Make sure you have placed this script in the Bipbip folder")

#A "Backup" folder is created where Haricot and Mais folders are stored
shutil.copytree(os.getcwd(), 'Backup', ignore=shutil.ignore_patterns('*.py'))

print("\nA Backup folder is created where Haricot and Mais Images (including Masks) are saved")

if not os.path.exists("Splits"):
	os.mkdir("Splits")

#Creating txt ("train" and "val") where Haricot images name are stored (80% train 20% val)
dirs=os.path.join(os.getcwd(),'Haricot/Images')
l = os.listdir(dirs)

random.seed(1234)
random.shuffle(l)

with open("Splits/train.txt", "w+") as f: 
	for i in range(72):
		f.write(l[i].split(".")[0])
		f.write("\n")

with open("Splits/val.txt", "w+") as f: 
	for i in range(72,90):
		f.write(l[i].split(".")[0])
		f.write("\n")

#Appending to the txt ("train" and "val") Mais images (80% train 20% val)
dirs=os.path.join(os.getcwd(),'Mais/Images')
l = os.listdir(dirs)

random.seed(1234)
random.shuffle(l)

with open("Splits/train.txt", "a") as f: 
	for i in range(72):
		f.write(l[i].split(".")[0])
		if(i != 71):
			f.write("\n")

with open("Splits/val.txt", "a") as f: 
	for i in range(72,90):
		f.write(l[i].split(".")[0])
		if(i != 89):
			f.write("\n")

#Creating a Masks folder where all masks from Haricot and Mais are stored
if not os.path.exists("Masks"):
	os.mkdir("Masks")

#Moving Mais masks from the original folder to Masks
source_dir = os.path.join(os.getcwd(),'Mais/Masks')
target_dir = os.path.join(os.getcwd(),'Masks')

file_names = os.listdir(source_dir)

for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

#Moving Haricot masks from the original folder to Masks
source_dir = os.path.join(os.getcwd(),'Haricot/Masks')
target_dir = os.path.join(os.getcwd(),'Masks')

file_names = os.listdir(source_dir)

for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)


#Creating a Images folder where all images from Haricot and Mais are stored
if not os.path.exists("Images"):
	os.mkdir("Images")

#Moving Mais images from the original folder to Images
source_dir = os.path.join(os.getcwd(),'Mais/Images')
target_dir = os.path.join(os.getcwd(),'Images')

file_names = os.listdir(source_dir)

for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

#Moving Haricot images from the original folder to Images
source_dir = os.path.join(os.getcwd(),'Haricot/Images')
target_dir = os.path.join(os.getcwd(),'Images')

file_names = os.listdir(source_dir)

for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

#Deleting original Mais and Haricot folders
shutil.rmtree('Mais', ignore_errors=True)
shutil.rmtree('Haricot', ignore_errors=True)

