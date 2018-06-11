# Deeplab V3+ for custom dataset

**Original deeplab v3+ code is https://github.com/tensorflow/models/tree/master/research/deeplab**

1. collect all data
2. merge data folders
3. generate SegRaw that has border line, 255, between labels
4. generate split table
5. move the data to deeplab/dataset/myset
6. goto deeplab/datasets
7. edit segmentation\_dataset.py to include my dataset
8. convert the image data and segmentation label to tfrecord format
9. goto deeplab
10. edit train.py to include 'max\_to\_keep' if you want to keep more than recent 5 check point
11. run train\_my.sh
12. run overlay.py if you want to check overlaid images

Place codes in the same directory as original deeplab v3+

Assumed tensorflow/models/research and tensorflow/models/research/slim paths are in PYTHONPATH

Assumed pascal voc dataset and frozen model are in deeplab/datasets/pascal_voc_seg


