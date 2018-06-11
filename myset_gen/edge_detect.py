
import numpy as np
from matplotlib import pyplot as plt
import scipy.misc

np.set_printoptions(threshold=np.inf)

def label_edge(img_path):
    img = scipy.misc.imread(img_path)
    col_dim = img.shape[0]
    row_dim = img.shape[1]

    edge_x=np.zeros((col_dim,row_dim),dtype=np.uint8)
    edge_y=np.zeros((col_dim,row_dim),dtype=np.uint8)


    # Example here is showing label 2 is small object so you don't want to lose any single pixel from the label
    for i in range(row_dim-1):
        edge_x_temp_i=((img[:,i] != img[:,i+1]) & (img[:,i] != 2))*255
        edge_x_temp_ip1 = ((img[:,i] != img[:,i+1]) & (img[:,i] == 2))*255
        edge_x[:,i]=edge_x[:,i] | edge_x_temp_i
        edge_x[:,i+1]=edge_x[:,i+1] | edge_x_temp_ip1

    for i in range(col_dim-1):
        edge_y_temp_i=((img[i,:] != img[i+1,:]) & (img[i,:] != 2))*255
        edge_y_temp_ip1 = ((img[i,:] != img[i+1,:]) & (img[i,:] == 2))*255
        edge_y[i,:]=edge_y[i,:] | edge_y_temp_i
        edge_y[i+1,:]=edge_y[i+1,:] | edge_y_temp_ip1

    edge_xy = edge_x | edge_y
    edged = edge_xy | img

    return edged

if __name__ == '__main__':

    img_path='./deeplab/datasets/myset/ImageSeg/000000.png'
    label_edged=label_edge(img_path)
    label_ori=scipy.misc.imread(img_path)

    plt.subplot(121),plt.imshow(label_ori)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(label_edged)
    plt.title('Edge overlayed Image'), plt.xticks([]), plt.yticks([])

    plt.show()


