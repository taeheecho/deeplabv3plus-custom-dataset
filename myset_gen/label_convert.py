import scipy.misc
from matplotlib import pyplot as plt
import numpy as np
import os.path
from glob import glob

np.set_printoptions(threshold=np.inf)

def gen_new_label(original_folder):

    for image_file in glob(os.path.join(original_folder,'*.png')):
        
        label_image = scipy.misc.imread(image_file)[:,:,0]
        print("generate new label for: ",image_file, label_image.shape)
        
        label_image_new = np.zeros(label_image.shape, dtype=np.uint8) #background

        label_image_new[(label_image == 7) | (label_image == 6)] = np.uint8(1) #road
    
        vehicle_pixels = (label_image == 10)
        vehicle_pixels[496:600,:]=False
        label_image_new[vehicle_pixels] = np.uint8(2) #car
        #print(label_image_new)
        
        yield os.path.basename(image_file), label_image_new

original_label_folder = '/home/taeheecho/Work/Lyft/carla_800_600_combined/CameraSeg'
new_label_folder = '/home/taeheecho/Work/Lyft/carla_800_600_combined/CameraSegNew'
if not os.path.exists(new_label_folder):
    os.makedirs(new_label_folder)

image_outputs = gen_new_label(original_label_folder)
for name, image in image_outputs:
    print("Saving ... ",name, image.shape)
    scipy.misc.imsave(os.path.join(new_label_folder, name), image)
