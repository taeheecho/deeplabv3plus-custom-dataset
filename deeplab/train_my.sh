#!/bin/bash
# Copyright 2018 The TensorFlow Authors All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
#
# This script is used to run local test on PASCAL VOC 2012 using MobileNet-v2.
# Users could also modify from this script for their use case.
#
# Usage:
#   # From the tensorflow/models/research/deeplab directory.
#   sh ./local_test_mobilenetv2.sh
#
#

# Exit immediately if a command exits with a non-zero status.
set -e

# Move one-level up to tensorflow/models/research directory.
cd ..

# Update PYTHONPATH.
###export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

# Set up the working environment.
CURRENT_DIR=$(pwd)
###WORK_DIR="${CURRENT_DIR}/deeplab"

# Run model_test first to make sure the PYTHONPATH is correctly set.
###python "${WORK_DIR}"/model_test.py -v

# Go to datasets folder and download PASCAL VOC 2012 segmentation dataset.
DATASET_DIR="datasets"
###cd "${WORK_DIR}/${DATASET_DIR}"
###sh download_and_convert_voc2012.sh

# Go back to original directory.
cd "${CURRENT_DIR}"

# Set up the working directories.
###PASCAL_FOLDER="pascal_voc_seg"
EXP_FOLDER="${CURRENT_DIR}/deeplab/datasets/myset/run_test"
INIT_FOLDER="${CURRENT_DIR}/deeplab/datasets/pascal_voc_seg/frozen_model/deeplabv3_mnv2_pascal_train_aug"
TRAIN_LOGDIR="${EXP_FOLDER}/train"
EVAL_LOGDIR="${EXP_FOLDER}/eval"
VIS_LOGDIR="${EXP_FOLDER}/vis"
EXPORT_DIR="${EXP_FOLDER}/export"
###mkdir -p "${INIT_FOLDER}"
mkdir -p "${TRAIN_LOGDIR}"
mkdir -p "${EVAL_LOGDIR}"
mkdir -p "${VIS_LOGDIR}"
mkdir -p "${EXPORT_DIR}"

# Copy locally the trained checkpoint as the initial checkpoint.
###TF_INIT_ROOT="http://download.tensorflow.org/models"
###CKPT_NAME="deeplabv3_mnv2_pascal_train_aug"
###TF_INIT_CKPT="${CKPT_NAME}_2018_01_29.tar.gz"
###cd "${INIT_FOLDER}"
###wget -nd -c "${TF_INIT_ROOT}/${TF_INIT_CKPT}"
###tar -xf "${TF_INIT_CKPT}"
cd "${CURRENT_DIR}"

###PASCAL_DATASET="${WORK_DIR}/${DATASET_DIR}/${PASCAL_FOLDER}/tfrecord"
MY_DATASET="${CURRENT_DIR}/deeplab/datasets/carla_aug/tfrecord"

# Train 20000 iterations.
NUM_ITERATIONS=500
python "${CURRENT_DIR}/deeplab"/train.py \
  --logtostderr \
  --dataset="my_data" \
  --initialize_last_layer=False \
  --last_layers_contain_logits_only=True \
  --train_split="train" \
  --model_variant="mobilenet_v2" \
  --output_stride=16 \
  --train_crop_size=600 \
  --train_crop_size=800 \
  --train_batch_size=4 \
  --training_number_of_steps="${NUM_ITERATIONS}" \
  --slow_start_step=0 \
  --slow_start_learning_rate=1e-6 \
  --fine_tune_batch_norm=False \
  --save_summaries_images=True \
  --tf_initial_checkpoint="${INIT_FOLDER}/model.ckpt-30000" \
  --train_logdir="${TRAIN_LOGDIR}" \
  --dataset_dir="${MY_DATASET}" \
  --base_learning_rate=1e-3 \
  --learning_rate_decay_factor=0.1 \
  --learning_rate_decay_step=400 \
  --save_interval_secs=60 \
  --max_to_keep=20 \
  --log_steps=1

# Run evaluation. This performs eval over the full val split (1449 images) and
# will take a while.
# Using the provided checkpoint, one should expect mIOU=75.34%.
python "${CURRENT_DIR}/deeplab"/eval.py \
  --logtostderr \
  --dataset="my_data" \
  --eval_split="val" \
  --model_variant="mobilenet_v2" \
  --eval_crop_size=600 \
  --eval_crop_size=800 \
  --checkpoint_dir="${TRAIN_LOGDIR}" \
  --eval_logdir="${EVAL_LOGDIR}" \
  --dataset_dir="${MY_DATASET}" \
  --max_number_of_evaluations=1 \
  --eval_batch_size=4

# Visualize the results.
python "${CURRENT_DIR}/deeplab"/vis.py \
  --logtostderr \
  --dataset="my_data" \
  --vis_split="val" \
  --model_variant="mobilenet_v2" \
  --vis_crop_size=600 \
  --vis_crop_size=800 \
  --checkpoint_dir="${TRAIN_LOGDIR}" \
  --vis_logdir="${VIS_LOGDIR}" \
  --dataset_dir="${MY_DATASET}" \
  --max_number_of_iterations=1 \
  --vis_batch_size=4 \
  --also_save_raw_predictions=True

# Export the trained checkpoint.
CKPT_PATH="${TRAIN_LOGDIR}/model.ckpt-${NUM_ITERATIONS}"
EXPORT_PATH="${EXPORT_DIR}/frozen_inference_graph.pb"

python "${CURRENT_DIR}/deeplab"/export_model.py \
  --logtostderr \
  --checkpoint_path="${CKPT_PATH}" \
  --export_path="${EXPORT_PATH}" \
  --model_variant="mobilenet_v2" \
  --num_classes=4 \
  --crop_size=600 \
  --crop_size=800 \
  --inference_scales=1.0

# Run inference with the exported checkpoint.
# Please refer to the provided deeplab_demo.ipynb for an example.
