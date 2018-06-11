collect all data
merge data folders
generate SegRaw that has border line, 255, between labels
generate split table
move the data to deeplab/dataset/myset
goto deeplab/datasets
edit segmentation_dataset.py to include my dataset 
convert the image data and segmentation label to tfrecord format
goto deeplab
edit train.py to include 'max_to_keep' if you want to keep more than recent 5 check points
run train_my.sh
run overlay.py if you want to check overlaid images
