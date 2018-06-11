from os import walk
import os
import shutil

RGB_destination = '../deeplab/datasets/myset/ImageRGB'
SEG_destination = '../deeplab/datasets/myset/ImageSeg'
SKIP_COUNT = 30 #Collected Imageset settling time such as first turn on of camera or new start of simulation

if os.path.exists(RGB_destination):
    shutil.rmtree(RGB_destination)
os.makedirs(RGB_destination)

if os.path.exists(SEG_destination):
    shutil.rmtree(SEG_destination)
os.makedirs(SEG_destination)

file_count=0
path ="./dataset_colletected"
for root, directories, filenames in os.walk(path):
    for directory in directories:
        if directory == 'ImageRGB':
            src_rgb_path = os.path.join(root,directory)
            src_seg_path = os.path.join(root,'ImageSeg')
            print(src_seg_path)
            src_rgb_files =  (os.listdir(src_rgb_path))
                for src_file in src_rgb_files:
                file_name_base = os.path.basename(src_file).rsplit('.',1)[0]
                if (int(file_name_base) < SKIP_COUNT):
                    continue
                full_seg_name = os.path.join(src_seg_path,src_file)
                if os.path.isfile(full_seg_name):
                    full_rgb_name = os.path.join(src_rgb_path,src_file)
                    dest_filename = '{:0>6}'.format(file_count)+'.png'
                    shutil.copy(full_rgb_name,os.path.join(RGB_destination,dest_filename))
                    shutil.copy(full_seg_name,os.path.join(SEG_destination,dest_filename))
                    file_count += 1

