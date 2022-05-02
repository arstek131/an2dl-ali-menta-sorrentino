#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import shutil
import sys
import glob
import random

# macros
DEBUG = 1
NO_MASK = 0
ALL_MASK = 1
SOME_MASK = 2


def main():
    ## init variables ##
    if(len(sys.argv) < 2):
        print("Insert number of images to be used for training set as argument")
        sys.exit()

    tot_num_images = len(glob.glob1("./training", "*.jpg"))
    num_images_training = int(sys.argv[1])
    num_images_validation = tot_num_images - num_images_training
    if(DEBUG):
        print("Images to be used for training: " + str(num_images_training))
        print("Images to be used for validation: " + str(num_images_validation))
        print("")

    ### creating main dataset structure ###
    print("Creating main dataset structure...")
    dataset_dir = os.getcwd()
    if(DEBUG):
        print(dataset_dir)

    # training directory
    training_dir = os.path.join(dataset_dir, 'training')
    if(DEBUG):
        print(training_dir)
    if not os.path.exists(training_dir):
        os.makedirs(training_dir)
    print(training_dir, "[OK]")

    # validation set directory
    validation_dir = os.path.join(dataset_dir, 'validation')
    if(DEBUG):
        print(validation_dir)
    if not os.path.exists(validation_dir):
        os.makedirs(validation_dir)
    print(validation_dir, "[OK]")

    # test set directory
    test_dir = os.path.join(dataset_dir, 'test')
    if(DEBUG):
        print(test_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    print(test_dir, "[OK]")

    ### creating dataset categorical folders ###
    # training
    no_mask_dir_training = os.path.join(training_dir, 'NO_MASK')
    if(DEBUG):
        print(no_mask_dir_training)
    if not os.path.exists(no_mask_dir_training):
        os.makedirs(no_mask_dir_training)
    print(no_mask_dir_training, "[OK]")

    all_mask_dir_training = os.path.join(training_dir, 'ALL_MASK')
    if(DEBUG):
        print(all_mask_dir_training)
    if not os.path.exists(all_mask_dir_training):
        os.makedirs(all_mask_dir_training)
    print(all_mask_dir_training, "[OK]")

    some_mask_dir_training = os.path.join(training_dir, 'SOME_MASK')
    if(DEBUG):
        print(some_mask_dir_training)
    if not os.path.exists(some_mask_dir_training):
        os.makedirs(some_mask_dir_training)
    print(some_mask_dir_training, "[OK]")

    # validation
    no_mask_dir_validation = os.path.join(validation_dir, 'NO_MASK')
    if(DEBUG):
        print(no_mask_dir_validation)
    if not os.path.exists(no_mask_dir_validation):
        os.makedirs(no_mask_dir_validation)
    print(no_mask_dir_validation, "[OK]")

    all_mask_dir_validation = os.path.join(validation_dir, 'ALL_MASK')
    if(DEBUG):
        print(all_mask_dir_validation)
    if not os.path.exists(all_mask_dir_validation):
        os.makedirs(all_mask_dir_validation)
    print(all_mask_dir_validation, "[OK]")

    some_mask_dir_validation = os.path.join(validation_dir, 'SOME_MASK')
    if(DEBUG):
        print(some_mask_dir_validation)
    if not os.path.exists(some_mask_dir_validation):
        os.makedirs(some_mask_dir_validation)
    print(some_mask_dir_validation, "[OK]")

    ### moving images to according folders ###
    """ for each couple { IMG_NAME, CATEGORICAL_NUMBER }
        if CATEGORY = 0		put image inside XX folder
        else if CATEGORY = 1 	put image inside XX folder
        else if CATEGORY = 2  put image inside XX folder
        else 					display error
    """
    with open('train_gt.json') as json_file:
        data = json.load(json_file)     # loading json from file to variable
        # taking all keys form json
        img_names = list(data.keys())
        # shuffling keys to obtain uniformity of classes distribution
        random.shuffle(img_names)

        # {IMG_NAME, CATEGORICAL_NUMBER}
        for img in img_names[:num_images_training]:
            img_name = img
            img_category = data[img_name]
            if(DEBUG):
                print(img_name, img_category)
            if(img_category == NO_MASK):
                if(DEBUG):
                    #print("NO MASK")
                    print("Target dir:", no_mask_dir_training)
                target_dir = no_mask_dir_training

            elif(img_category == ALL_MASK):
                if(DEBUG):
                    #print("ALL MASK")
                    print("Target dir:", all_mask_dir_training)
                target_dir = all_mask_dir_training

            elif(img_category == SOME_MASK):
                if(DEBUG):
                    #print("SOME MASK")
                    print("Target dir:", some_mask_dir_training)
                target_dir = some_mask_dir_training

            else:
                if(DEBUG):
                    print("Wrong categorical value")

            shutil.move(os.path.join(training_dir, img_name), target_dir)

        # {IMG_NAME, CATEGORICAL_NUMBER}
        for img in img_names[num_images_training:]:
            img_name = img
            img_category = data[img_name]
            if(DEBUG):
                print(img_name, img_category)
            if(img_category == NO_MASK):
                if(DEBUG):
                    #print("NO MASK")
                    print("Target dir:", no_mask_dir_validation)
                target_dir = no_mask_dir_validation

            elif(img_category == ALL_MASK):
                if(DEBUG):
                    #print("ALL MASK")
                    print("Target dir:", all_mask_dir_validation)
                target_dir = all_mask_dir_validation

            elif(img_category == SOME_MASK):
                if(DEBUG):
                    #print("SOME MASK")
                    print("Target dir:", some_mask_dir_validation)
                target_dir = some_mask_dir_validation

            else:
                if(DEBUG):
                    print("Wrong categorical value")

            shutil.move(os.path.join(training_dir, img_name), target_dir)
    return 0


if __name__ == "__main__":
    main()
