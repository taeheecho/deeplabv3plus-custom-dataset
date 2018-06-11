import scipy.misc
from matplotlib import pyplot as plt
import numpy as np
import os.path
from glob import glob
from edge_detect import label_edge


def gen_new_label(original_folder):

    for image_file in glob(os.path.join(original_folder,'*.png')):
        
        label_image_new = label_edge(image_file)
        
        yield os.path.basename(image_file), label_image_new

original_label_folder = './deeplab/datasets/myset/ImageSeg' 
new_label_folder ='./deeplab/datasets/myset/ImageSegRaw'
if not os.path.exists(new_label_folder):
    os.makedirs(new_label_folder)

image_outputs = gen_new_label(original_label_folder)
for name, image in image_outputs:
    print("Saving ... ",name, image.shape)
    scipy.misc.imsave(os.path.join(new_label_folder, name), image)
