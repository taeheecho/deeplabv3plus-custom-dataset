from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
from scipy import misc
import glob
import os.path

src_names = glob.glob('./datasets/myset/Model/vis/segmentation_results/*image.png')
for src_name in src_names:
    basename=src_name.rsplit('_',1)[0]
    pred_name=os.path.join(basename+'_prediction.png')

    src = misc.imread(src_name)
    pred = misc.imread(pred_name)
    plt.imshow(src)
    plt.imshow(pred, alpha=0.6)
    plt.show()
