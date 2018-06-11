from os import walk
import os
import os.path
import shutil
import random

RGB_destination = './deeplab/dataset/myset/ImageRGB'

file_names = os.listdir(RGB_destination)
train_set=[]
for file_name in file_names:
    train_set.append(os.path.basename(file_name).rsplit('.',1)[0])

file_trainval=open("./deeplab/dataset/myset/Split/trainval.txt","w")
file_length = len(train_set)
for i in range(file_length):
    file_trainval.write(train_set[i]+"\n")
file_trainval.close()

print("len_total = ", len(train_set))
NUM_Train_percent = 0.7
NUM_Val_percent = 0.3

len_train = int(file_length*NUM_Train_percent)
len_val = file_length - len_train 

val_set = []
for i in range(len_val):
    j = random.randint(0,file_length-1)
    val_set.append(train_set[j])
    train_set.remove(train_set[j])
    file_length -= 1

print("train_set: ", len(train_set))
print("val_set: ", len(val_set))

file_train=open("./deeplab/dataset/myset/Split/train.txt","w")
file_length = len(train_set)
for i in range(file_length):
    file_train.write(train_set[i]+"\n")
file_train.close()

file_val=open("./deeplab/dataset/myset/Split/val.txt","w")
file_length = len(val_set)
for i in range(file_length):
    file_val.write(val_set[i]+"\n")
file_val.close()

